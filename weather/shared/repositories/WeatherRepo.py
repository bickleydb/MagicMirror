import datetime
from weather.models.DailyWeatherModel import DailyWeatherModel
from weather.models.WeatherForcastModel import WeatherForcastModel
from weather.shared.owm_objects.OWMRequest import OWMRequest
from weather.models.WeatherForcastModel import WeatherForcastModel
from weather.models.WeatherConfigurationUserBridge import WeatherConfigurationUserBridge as WCUB


class WeatherRepo:

    def get_user_location(self, user):
        locationList = WCUB.get_manager()
        rtnList = []
        for bridge in locationList.filter(user=user):
            rtnList.append(bridge.weatherConfiguration)
        return rtnList

    def get_today(self):
        return datetime.date.today()

    def get_today_weather(self, user):
        currentLocation = self.get_user_location(user)[0]
        weather_manager = DailyWeatherModel.get_manager()
        today_weather = weather_manager.all().filter(date=self.get_today())
        weather_data = today_weather.filter(location=currentLocation)
        if len(weather_data) is 0:
            self.updateToday(user)
            weather_data = weather_manager.all().filter(date=self.get_today())
        return weather_data[0]

    def updateToday(self, user):
        currentLocation = self.get_user_location(user)[0]
        data = OWMRequest(zip_code=currentLocation.zipCode).get_data()
        weather_manager = DailyWeatherModel.get_manager()
        sunrise = data.get_sunrise_time()
        sunset = data.get_sunset_time()
        weather_record, _ = weather_manager.update_or_create(
                date=str(self.get_today()),
                defaults={
                     "location": currentLocation,
                     "description": data.get_weather_desc(),
                     "high_temp": data.get_max_temp(),
                     "low_temp": data.get_min_temp(),
                     "main_temp": data.get_temp(),
                     "wind_direct": data.get_wind_deg(),
                     "icon_key": data.get_weather_icon(),
                     "humidity": data.get_humidity(),
                     "wind_speed": data.get_wind_speed(),
                     "sunrise": datetime.datetime.fromtimestamp(sunrise),
                     "sunset": datetime.datetime.fromtimestamp(sunset),
                }
        )
        weather_record.save()

    def updateForcast(self):
        response_data = OWMRequest(should_get_forcast=True).get_data()
        weather_manager = WeatherForcastModel.get_manager()
        dayList = response_data.getDayList()
        timezone = datetime.timezone(datetime.timedelta(hours=-8))
        for dayValue in dayList:
            secondsSinceEpoch = dayValue.getSecondsSinceEpoch()
            dateTimeValue = datetime.datetime.fromtimestamp(secondsSinceEpoch)
            dateTimeValue = dateTimeValue.astimezone(timezone)
            weather_record, _ = weather_manager.update_or_create(
                dateTime=dateTimeValue,
                defaults={
                    "high_temp": dayValue.getHighTemp(),
                    "main_temp": dayValue.getMainTemp(),
                    "low_temp": dayValue.getLowTemp(),
                    "wind_speed": dayValue.getWindSpeed()
                }
            )
            weather_record.save()
