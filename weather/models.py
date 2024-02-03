from django.db import models


# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=200)
    lat = models.DecimalField(max_digits=9, decimal_places=7)
    lon = models.DecimalField(max_digits=10, decimal_places=7)

    def __str__(self):
        return self.name
