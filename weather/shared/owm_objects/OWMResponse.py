from . import OWMCloudValues
from . import OWMCoordinateValues
from . import OWMMainValues
from . import OWMSunValues
from . import OWMWeatherValues
from . import OWMWindValues


class OWMResponse:
    def __init__(self, jsonValue):
        print(jsonValue)
        coordinates = jsonValue["coord"]
        weather_list = jsonValue["weather"]
        self.jsonValue = jsonValue
        self.weather_list = []

        self.sun_values = OWMSunValues.OWMSunValues(
            sunrise_time=jsonValue["sys"]["sunrise"],
            sunset_time=jsonValue["sys"]["sunset"]
        )

        self.cloud_object = OWMCloudValues.OWMCloudValues(
            cloud_status=jsonValue["clouds"]["all"]
        )

        self.wind_object = OWMWindValues.OWMWindValues(
            date=jsonValue["dt"],
            wind_speed=jsonValue["wind"]["speed"],
        )

        self.main_weather = OWMMainValues.OWMMainValues(
            date=jsonValue["dt"],
            temp=jsonValue["main"]["temp"],
            pressure=jsonValue["main"]["pressure"],
            humid=jsonValue["main"]["humidity"],
            max_temp=jsonValue["main"]["temp_max"],
            min_temp=jsonValue["main"]["temp_min"],
        )

        for i in range(0, len(weather_list)):
            self.weather_list.append(OWMWeatherValues.OWMWeatherValues(
                date=jsonValue["dt"],
                weather_id=weather_list[i]["id"], 
                weather_main=weather_list[i]["main"],
                desc=weather_list[i]["description"],
                icon=weather_list[i]["icon"]
            ))

        self.coordinates = OWMCoordinateValues.OWMCoordinateValues(
            latitude=coordinates["lat"], 
            longitude=coordinates["lon"]
        )

    def get_sunrise_time(self):
        return self.sun_values.get_sunrise_time()

    def get_sunset_time(self):
        return self.sun_values.get_sunset_time()

    def get_wind_speed(self):
        return self.wind_object.get_wind_speed()

    def get_wind_deg(self):
        return self.wind_object.get_wind_deg()

    def get_cloud_status(self):
        return self.cloud_object.get_cloud_status()

    def get_temp(self):
        return self.main_weather.get_temp()

    def get_pressure(self):
        return self.main_weather.get_pressure()

    def get_humidity(self):
        return self.main_weather.get_humidity()

    def get_min_temp(self):
        return self.main_weather.get_min_temp()

    def get_max_temp(self):
        return self.main_weather.get_max_temp()

    def get_weather_id(self):
        return self.weather_list[0].get_weather_id()

    def get_weather_main(self):
        return self.weather_list[0].get_weather_main()

    def get_weather_desc(self):
        return self.weather_list[0].get_weather_desc()

    def get_weather_icon(self):
        return self.weather_list[0].get_weather_icon()

    def get_longitude(self):
        return self.coordinates.get_longitude()

    def get_latitude(self):
        return self.coordinates.get_latitude()

    def __str__(self):
        return self.jsonValue
