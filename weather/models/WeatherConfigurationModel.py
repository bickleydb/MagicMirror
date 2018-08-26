from django.db import models
from django.utils.translation import gettext as _

from . import Location_Max_Length
from . import Zip_Code_Max_Length
class WeatherConfigurationModel(models.Model):

    zipCode = models.CharField(max_length=Zip_Code_Max_Length, 
            help_text=_("Zip code to retrieve weather data for")
    )

    locationName = models.CharField(max_length=Location_Max_Length,
            help_text=_("Human readable name of location")
    )
    
    def __str__(self):
        return self.locationName
