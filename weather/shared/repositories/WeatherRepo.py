import datetime

from weather.models.DailyWeatherModel import DailyWeatherModel
from weather.models.WeatherForcastModel import WeatherForcastModel
from weather.shared.owm_objects.OWMRequest import OWMRequest

from weather.models.WeatherConfigurationUserBridge import WeatherConfigurationUserBridge as WCUB
class WeatherRepo:

    def get_user_location(self, user):
        locationList = WCUB.get_manager()
        rtnList = []
        for bridge in locationList.filter(user=user):
            rtnList.append(bridge.weatherConfiguration)
        return rtnList


    def get_today_date(self):
        return datetime.date.today()

    def get_today_weather(self, user):
        currentLocation = self.get_user_location(user)[0]
        weather_manager = DailyWeatherModel.get_manager()
        weather_data = weather_manager.all().filter(date=self.get_today_date()).filter(location=currentLocation)
        if len(weather_data) is 0:
            self.updateToday(user)
            weather_data = weather_manager.all().filter(date=self.get_today_date())
        return weather_data[0]

    def updateToday(self, user):
        currentLocation = self.get_user_location(user)[0]
        response_data = OWMRequest(zip_code=currentLocation.zipCode).get_data()
        weather_manager = DailyWeatherModel.get_manager()
        weather_record, _ = weather_manager.update_or_create(
                date     = str(self.get_today_date()),
                defaults = {
                     "location"     : currentLocation,
                     "description" : response_data.get_weather_desc(),
                     "high_temp"   : response_data.get_max_temp(),
                     "low_temp"    : response_data.get_min_temp(),
                     "main_temp"   : response_data.get_temp(),
                     "wind_direct" : response_data.get_wind_deg(),
                     "icon_key"    : response_data.get_weather_icon(),
                     "humidity"    : response_data.get_humidity(),
                     "wind_speed"  : response_data.get_wind_speed(),
                     "sunrise"     : datetime.datetime.fromtimestamp(response_data.get_sunrise_time()),
                     "sunset"      : datetime.datetime.fromtimestamp(response_data.get_sunset_time()),
                }
        )
        weather_record.save()

    def updateForcast(self):
        response_data = OWMRequest(should_get_forcast=True).get_data()
        weather_manager = DailyWeatherModel.get_manager()
        dayList = response_data.getDayList()
        for dayValue in dayList:
            weather_record, _ = weather_manager.update_or_create(
                date = datetime.datetime.fromtimestamp(dayValue.getSecondsSinceEpoch()),
                defaults = {
                    "description" : dayValue.getDescription(),
                    "high_temp"   : dayValue.getHighTemp(),
                    "main_temp"   : dayValue.getMainTemp(),
                    "humidity"    : dayValue.getHumidity(),
                    "low_temp"    : dayValue.getLowTemp(),
                    "wind_speed"  : dayValue.getWindSpeed()
                }
            )
            weather_record.save()
        
        
