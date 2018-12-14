from django.shortcuts import render
from django.template import loader


class WeatherDayResponse:

    def __init__(self, weather):
        self.weatherObject = weather

    def ConvertKelvinToFaren(self, value):
        return (value * 9)/5 - 459.67

    def toHttp(self):
        template = loader.get_template('weather/widget/new_template.html')
        main_temp = self.weatherObject.main_temp
        high_temp = self.weatherObject.high_temp
        return template.render({
            "main_temp": self.ConvertKelvinToFaren(main_temp),
            "high_temp": self.ConvertKelvinToFaren(high_temp),
            "low_temp": self.ConvertKelvinToFaren(self.weatherObject.low_temp),
            "sunrise": self.weatherObject.sunrise,
            "snow_amt": self.weatherObject.snow_amt,
            "rain_amt": self.weatherObject.rain_amt,
            "sunset": self.weatherObject.sunset,
            "wind_speed": self.weatherObject.wind_speed,
            "description": self.weatherObject.description,
            "humidity": self.weatherObject.humidity,
            "icon": self.weatherObject.icon_key,
            "tempUnit": "°F",
        })
