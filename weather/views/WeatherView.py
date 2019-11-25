from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User

import datetime

from weather.shared.repositories.WeatherRepo import WeatherRepo

from MagicMirror.shared.MagicMirrorView.MagicMirrorView import \
    MagicMirrorView as MMV

from weather.shared.ConversionFunctions import ConvertingFunctions


class WeatherView:

    def __init__(self):
        self.weatherRepo = WeatherRepo()

    def get_weather(self, request):
        if request.user is None:
            return MMV.get_bad_request("Needs Logged In User")
        return HttpResponse(self.weatherRepo.updateToday(request.user))

    def update_today(self, request):
        if request.user is None:
            return MMV.get_bad_request("Needs Logged In User")
        self.weatherRepo.update_today(request.user)
        return HttpResponse(True)

    def update_forcast(self, request):
        if request.user is None:
            return MMV.get_bad_request("Needs Logged In User")
        forcast = self.weatherRepo.get_forcast(request.user)
        return HttpResponse(True)

    def get_default_user(self):
        return User.objects.get(username="daniel")

    def force_update(self, request):
        self.weatherRepo.update_forcast(self.get_default_user())
        return HttpResponse(True)

    def get_forcast(self, request):
        current_date = datetime.today()

    def forcast_view(self, request):
        forcast_values = self.get_forcast_data(request.user)
        template = loader.get_template('weather/widget/weather_forcast.html')
        return HttpResponse(template.render({
            "date_list": forcast_values.values(),
            "unit_type": "°F",
        }))

    def get_forcast_data(self, user):
        forcast_values = self.weatherRepo.get_forcast(user)
        for forcast in forcast_values:
            kelvenTemp = forcast_values[forcast]["main_temp"]
            mainTemp = ConvertingFunctions.kelvinToFaren(kelvenTemp)
            forcast_values[forcast]["main_temp"] = mainTemp
        return forcast_values

    def index(self, request):
        template = loader.get_template('weather/widget/new_template.html')
        today_weather = self.weatherRepo.get_today_weather(request.user)
        farenMain = ConvertingFunctions.kelvinToFaren(today_weather.main_temp)
        farenHigh = ConvertingFunctions.kelvinToFaren(today_weather.high_temp)
        farenLow = ConvertingFunctions.kelvinToFaren(today_weather.low_temp)
        return HttpResponse(template.render({
            "main_temp": farenMain,
            "high_temp": farenHigh,
            "low_temp": farenLow,
            "sunrise": today_weather.sunrise,
            "snow_amt": today_weather.snow_amt,
            "rain_amt": today_weather.rain_amt,
            "sunset": today_weather.sunset,
            "wind_speed": today_weather.wind_speed,
            "description": today_weather.description,
            "humidity": today_weather.humidity,
            "icon": today_weather.icon_key,
            "tempUnit": "°F",
        }, request))
