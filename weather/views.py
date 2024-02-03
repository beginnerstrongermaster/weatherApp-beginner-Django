import requests
from django.http import request
from django.shortcuts import render, redirect

from weather.models import City


# Create your views here.

def weatherList(request):
    weather_data = []
    if request.method == "GET":
        # Get cities and find their weather infos by using weather API
        cities = City.objects.all()
        for city in cities:
            url = f"https://api.openweathermap.org/data/2.5/weather?lat={city.lat}&lon={city.lon}&appid={YourAPIKey}&units=metric"
            response = requests.get(url)
            data = response.json()

            weather = {
                "id": city.id,
                "city": data["name"],
                "temp": data["main"]["temp"],
                "description": data['weather'][0]['description'],
                "icon": data["weather"][0]["icon"]
            }

            weather_data.append(weather)
        return render(request, context={"weather_data": weather_data}, template_name="weather.html")

    if request.method == "POST":
        city_name = request.POST.get("city_name")
        city_name = city_name.capitalize()

        # Get city latitude and longitude by using API
        url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&appid={YourAPIKey}"
        response = requests.get(url)
        data = response.json()
        city = data[0]['name']
        lat = data[0]["lat"]
        lon = data[0]["lon"]

        # Save it to Database
        City.objects.create(name=city, lat=lat, lon=lon)
        return redirect("weather")


def weatherDelete(request,**kwargs):
    if request.method == "POST":
        city_id = kwargs['pk']
        print(city_id)
        queryset = City.objects.filter(id=city_id)
        print(queryset)
        queryset.delete()
    return redirect("weather")
