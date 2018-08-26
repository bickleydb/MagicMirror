from django.contrib import admin

from weather.models.DailyWeatherModel import DailyWeatherModel
from weather.models.WeatherConfigurationModel import WeatherConfigurationModel
from weather.models.WeatherConfigurationUserBridge import WeatherConfigurationUserBridge
# Register your models here.
admin.site.register(DailyWeatherModel)
admin.site.register(WeatherConfigurationModel)
admin.site.register(WeatherConfigurationUserBridge)

