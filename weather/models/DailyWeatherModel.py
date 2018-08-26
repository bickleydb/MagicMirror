from django.db import models

from . import Free_Text_Max_Length

class DailyWeatherModel(models.Model):

    date        = models.DateField(unique=True)
    description = models.CharField(max_length=Free_Text_Max_Length,
            blank=True,
            null=True
    )
    high_temp   = models.FloatField(blank=True,null=True) 
    main_temp   = models.FloatField(blank=True,null=True)
    humidity    = models.FloatField(blank=True,null=True)
    low_temp    = models.FloatField(blank=True,null=True)
    snow_amt    = models.FloatField(blank=True,null=True)
    rain_amt    = models.FloatField(blank=True,null=True)
    wind_speed  = models.FloatField(blank=True,null=True)
    wind_direct = models.IntegerField(blank=True,null=True)
    icon_key    = models.CharField(max_length=Free_Text_Max_Length,blank=True,null=True)
    sunrise     = models.TimeField(blank=True,null=True)
    sunset      = models.TimeField(blank=True,null=True)

    def __str__(self):
        return str(self.date)

    @staticmethod
    def get_manager():
        return DailyWeatherModel.objects

 

