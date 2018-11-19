from django.db import models

import uuid

from . import Name_Max_Length

class LocationModel(models.Model):

    readonly_fields  = ["uniqueId"]

    name = models.CharField(max_length=Name_Max_Length)
    county = models.CharField(max_length=Name_Max_Length)
    address = models.CharField(max_length=Name_Max_Length)
    city = models.CharField(max_length=Name_Max_Length)
    county = models.CharField(max_length=Name_Max_Length)
    postalCode = models.CharField(max_length=Name_Max_Length)

    uniqueId = models.UUIDField("Unique ID", default = uuid.uuid4, unique=True, editable=False)

    def get_manager():
        return LocationModel.objects

    def __str__(self):
        return self.name
