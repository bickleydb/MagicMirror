from django.db import models

class daily_weather(models.Model):

    def get_manager():
        return daily_weather.objects

    date        = models.DateField(unique=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    high_temp   = models.FloatField(blank=True,null=True) 
    main_temp   = models.FloatField(blank=True,null=True)
    humidity    = models.FloatField(blank=True,null=True)
    low_temp    = models.FloatField(blank=True,null=True)
    snow_amt    = models.FloatField(blank=True,null=True)
    rain_amt    = models.FloatField(blank=True,null=True)
    wind_speed  = models.FloatField(blank=True,null=True)
    wind_direct = models.IntegerField(blank=True,null=True)
    icon_key    = models.CharField(max_length=500,blank=True,null=True)
    sunrise     = models.TimeField(blank=True,null=True)
    sunset      = models.TimeField(blank=True,null=True)


class forcast_weather(models.Model):

    def get_manager():
        return forcast_weather.objects

    date        = models.DateField(unique=True,null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    high_temp   = models.FloatField(blank=True,null=True) 
    main_temp   = models.FloatField(blank=True,null=True)
    humidity    = models.FloatField(blank=True,null=True)
    low_temp    = models.FloatField(blank=True,null=True)
    snow_amt    = models.FloatField(blank=True,null=True)
    rain_amt    = models.FloatField(blank=True,null=True)
    wind_speed  = models.FloatField(blank=True,null=True)
