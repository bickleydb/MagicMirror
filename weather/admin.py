from django.contrib import admin

from weather.models.DailyWeatherModel import DailyWeatherModel
from weather.models.WeatherConfigurationModel import WeatherConfigurationModel
from weather.models.WeatherForcastModel import WeatherForcastModel

import weather.models.WeatherConfigurationUserBridge as WCB
# Register your models here.
admin.site.register(DailyWeatherModel)
admin.site.register(WeatherConfigurationModel)
admin.site.register(WCB.WeatherConfigurationUserBridge)
admin.site.register(WeatherForcastModel)