from django.db import models

from . import Name_Max_Length

class LocationModel(models.Model):

    name = models.CharField(max_length=Name_Max_Length)
    county = models.CharField(max_length=Name_Max_Length)
    address = models.CharField(max_length=Name_Max_Length)
    city = models.CharField(max_length=Name_Max_Length)
    county = models.CharField(max_length=Name_Max_Length)
    postalCode = models.CharField(max_length=Name_Max_Length)

    def get_manager():
        return LocationModel.objects

    def __str__(self):
        return self.name
