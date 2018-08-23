
from . import OWMMainValues, OWMWeatherValues, OWMWindValues, OWMCloudValues 

class OWMForcastSingleDay:
    def __init__(self, jsonData):
        self.parseMain(jsonData)


    def parseMain(self, jsonData):
        self.dateStr = jsonData["dt"]

        self.mainVals = OWMMainValues.OWMMainValues(
            temp=jsonData["main"]["temp"],
            pressure=jsonData["main"]["pressure"],
            humid=jsonData["main"]["humidity"],
            max_temp=jsonData["main"]["temp_max"],
            min_temp=jsonData["main"]["temp_min"]
        )

        self.windVals = OWMWindValues.OWMWindValues(
            wind_deg=jsonData["wind"]["deg"],
            wind_speed=jsonData["wind"]["speed"]
        ) 

        self.weatherVals = OWMWeatherValues.OWMWeatherValues(
            weather_id=jsonData["weather"][0]["id"],
            weather_main=jsonData["weather"][0]["main"],
            icon=jsonData["weather"][0]["icon"],
            desc=jsonData["weather"][0]["description"]
        )

    def getSecondsSinceEpoch(self):
        return self.dateStr

    def getDescription(self):
        return self.weatherVals.desc
    
    def getHighTemp(self):
        return self.mainVals.max_temp

    def getMainTemp(self):
        return self.mainVals.temp

    def getLowTemp(self):
        return self.mainVals.min_temp

    def getHumidity(self):
        return self.mainVals.humid

    def getWindSpeed(self):
        return self.windVals.wind_speed
