from django.db import models
from . import Free_Text_Max_Length
import datetime


class WeatherForcastModel(models.Model):

    timeZone = datetime.timezone(datetime.timedelta(hours=-8))

    ingestion_time = models.DateTimeField(auto_now=True, null=False)

    dateTime = models.DateTimeField(
        auto_now=False,
        auto_now_add=False,
        unique=True,
    )

    locationName = models.CharField(max_length=100, null=True)
    icon_key = models.CharField(
        max_length=Free_Text_Max_Length, blank=True, null=True)
    high_temp = models.FloatField(blank=True, null=True)
    main_temp = models.FloatField(blank=True, null=True)
    low_temp = models.FloatField(blank=True, null=True)
    snow_amt = models.FloatField(blank=True, null=True)
    rain_amt = models.FloatField(blank=True, null=True)
    wind_speed = models.FloatField(blank=True, null=True)

    @staticmethod
    def get_manager():
        return WeatherForcastModel.objects

    def __str__(self):
        return str(self.locationName) + " : " +  self.dateTime.astimezone(self.timeZone).strftime("%Y-%m-%d %H:%M")
    
    class Meta:
        ordering = ["dateTime"]
