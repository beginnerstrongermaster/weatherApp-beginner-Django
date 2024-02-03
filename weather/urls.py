from django.conf.urls.static import static
from django.urls import path

from weather import views
from weatherPro import settings

urlpatterns = [
    path('',views.weatherList,name='weather'),
    path('weather/delete/<int:pk>',views.weatherDelete,name='weather-delete'),
]

urlpatterns += static('weather/media/', document_root=settings.MEDIA_ROOT)
urlpatterns += static('weather/static/', document_root=settings.STATIC_ROOT)