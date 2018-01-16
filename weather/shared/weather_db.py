import datetime

from  weather.models.weather_models import daily_weather as dw
import weather.shared.owm_request as owmreq

class weather_repository:

    def get_today_date(self):
        return datetime.date.today()

    def get_today_weather(self):
        weather_manager = dw.get_manager()
        return list(weather_manager.all().filter(date=self.get_today_date()))[0]

    def updateToday(self):
        response_data = owmreq.owm_request().get_data()
        weather_manager = dw.get_manager()
        weather_record, _ = weather_manager.update_or_create(
                date     = str(self.get_today_date()),
                defaults = {
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