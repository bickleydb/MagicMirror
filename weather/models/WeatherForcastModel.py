from django.db import models
from . import Free_Text_Max_Length

class WeatherForcastModel(models.Model):

    date        = models.DateField(unique=True,null=True)
    description = models.CharField(max_length=Free_Text_Max_Length, blank=True, null=True)
    high_temp   = models.FloatField(blank=True,null=True) 
    main_temp   = models.FloatField(blank=True,null=True)
    humidity    = models.FloatField(blank=True,null=True)
    low_temp    = models.FloatField(blank=True,null=True)
    snow_amt    = models.FloatField(blank=True,null=True)
    rain_amt    = models.FloatField(blank=True,null=True)
    wind_speed  = models.FloatField(blank=True,null=True)

    @staticmethod
    def get_manager():
        return WeatherForcastModel.objects

