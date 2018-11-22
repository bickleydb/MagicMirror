from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader 


from weather.shared.repositories.WeatherRepo import WeatherRepo

def get_weather(request):
    weather_repo = WeatherRepo()
    return HttpResponse(weather_repo.updateToday(request.user))

def update_today(request):
    weather_repo = WeatherRepo()
    weather_repo.updateToday(request.user)
    return HttpResponse(True)


def update_forcast(request):
     weather_repo = WeatherRepo()
     weather_repo.updateForcast()
     return HttpResponse(True)

def index(request):
    weather_repo = WeatherRepo()
    template = loader.get_template('weather/widget/new_template.html')
    today_weather = weather_repo.get_today_weather(request.user)
    print (today_weather.rain_amt)
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
        "icon"    : today_weather.icon_key,
        "tempUnit" : "°F",
    },request))


   # snow_amt    = models.FloatField(blank=True,null=True)
   # rain_amt    = models.FloatField(blank=True,null=True)



class ConvertingFunctions:

    def kelvinToFaren(value):
        return (value * 9)/5 - 459.67