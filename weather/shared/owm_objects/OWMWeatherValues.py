class OWMWeatherValues:
    def __init__(self,
                 date=0,
                 weather_id=0,
                 weather_main="",
                 desc="",
                 icon=""):
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
        return self.get_weather_id

    def get_date(self):
        return self.date
