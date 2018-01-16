from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


import weather.shared.weather_db  as weather_db

def get_weather(request):
    weather_repo = weather_db.weather_repository()
    return HttpResponse(weather_repo.updateToday())

def update_today(request):
    weather_repo = weather_db.weather_repository()
    weather_repo.updateToday()
    return HttpResponse(True)


def index(request):
    weather_repo = weather_db.weather_repository()
    template = loader.get_template('weather/widget/weather_widget.html')
    today_weather = weather_repo.get_today_weather()
    return HttpResponse(template.render({
        "main_temp": ConvertingFunctions.kelvinToFaren(today_weather.main_temp),
        "high_temp": ConvertingFunctions.kelvinToFaren(today_weather.high_temp),
        "low_temp" : ConvertingFunctions.kelvinToFaren(today_weather.low_temp),
        "sunrise"  : today_weather.sunrise,
        "snow_amt": today_weather.snow_amt,
        "rain_amt" : today_weather.rain_amt,
        "sunset" : today_weather.sunset,
        "wind_speed" : today_weather.wind_speed,
        "description" : today_weather.description,
        "humidity" : today_weather.humidity,
    },request))


   # snow_amt    = models.FloatField(blank=True,null=True)
   # rain_amt    = models.FloatField(blank=True,null=True)



class ConvertingFunctions:

    def kelvinToFaren(value):
        return (value * 9)/5 - 459.67