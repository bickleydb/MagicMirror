
class owm_response:
    def __init__(self, jsonValue):
        coordinates = jsonValue["coord"]
        weather_list = jsonValue["weather"]
        self.jsonValue = jsonValue
        self.weather_list = []

    
        self.sun_values = openweathermap_sun_values(
            sunrise_time=jsonValue["sys"]["sunrise"],
            sunset_time=jsonValue["sys"]["sunset"]
        )


        self.cloud_object = openweathermap_cloud_object(
            cloud_status=jsonValue["clouds"]["all"]
        )

        self.wind_object = openweathermap_wind(
            date=jsonValue["dt"],
            wind_speed=jsonValue["wind"]["speed"],
            wind_deg=jsonValue["wind"]["deg"]
        )

        self.main_weather = openweathermap_main_weather(
            date=jsonValue["dt"],
            temp=jsonValue["main"]["temp"],
            pressure=jsonValue["main"]["pressure"],
            humid=jsonValue["main"]["humidity"],
            max_temp=jsonValue["main"]["temp_max"],
            min_temp=jsonValue["main"]["temp_min"],
        )
        
        for i in range(0,len(weather_list)):
            self.weather_list.append( openweathermap_weather_values(
                date=jsonValue["dt"],
                weather_id=weather_list[i]["id"], 
                weather_main=weather_list[i]["main"],
                desc=weather_list[i]["description"],
                icon=weather_list[i]["icon"]
                
            )  )
        

        self.coordinates = coordinate_pair(
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


class openweathermap_sun_values:
    def __init__(self, sunrise_time=0, sunset_time=0):
        self.sunrise = sunrise_time
        self.sunset = sunset_time

    def get_sunrise_time(self):
        return self.sunrise

    def get_sunset_time(self):
        return self.sunset

class openweathermap_cloud_object:
    def __init__(self, date=0, cloud_status=""):
        self.cloud_status_value = cloud_status
        self.date = date

    def get_cloud_status(self):
        return self.cloud_status_value

    def get_date(self):
        return self.date


class openweathermap_wind:
    def __init__(self, date=0, wind_speed=0, wind_deg=0):
        self.date = date
        self.wind_speed= wind_speed
        self.wind_deg = wind_deg
    
    def get_wind_speed(self):
        return self.wind_speed

    def get_wind_deg(self):
        return self.wind_deg

    def get_date(self):
        return self.date


class openweathermap_main_weather:
    def __init__(self, date=0, temp=0, pressure=0, humid=0, min_temp=0, max_temp=0):
        self.temp = temp
        self.pressure = pressure
        self.humid = humid
        self.min_temp = min_temp
        self.max_temp = max_temp
        self.date = date

    def get_temp(self):
        return self.temp

    def get_pressure(self):
        return self.pressure

    def get_humidity(self):
        return self.humid

    def get_min_temp(self):
        return self.min_temp

    def get_max_temp(self):
        return self.max_temp

    def get_date(self):
        return self.date

class openweathermap_weather_values:
    def __init__(self, date=0, weather_id=0, weather_main="", desc="", icon=""):
        self.date = date
        self.weather_id = weather_id
        self.weather_main = weather_main
        self.desc = desc
        self.icon = icon
    
    def get_weather_id(self):
        return self.weather_id

    def get_weather_main(self):
        return self.weather_main

    def get_weather_desc(self):
        return self.desc

    def get_weather_icon(self):
        return self.icon

    def get_date(self):
        return self.date

class coordinate_pair:
    def __init__(self, longitude=0, latitude=0):
        self.longitude = longitude
        self.latitude = latitude

    def get_longitude(self):
        return self.longitude

    def get_latitude(self):
        return self.latitude
