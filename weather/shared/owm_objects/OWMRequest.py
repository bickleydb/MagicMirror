import requests
import json

import weather.shared
import weather.shared.owm_objects.OWMResponse as owmr
import weather.shared.owm_objects.OWMForcastResponse as owmrf

class OWMRequest:

    weather_pattern = "http://api.openweathermap.org/data/2.5/weather?zip={},{}&appid={}"
    forcast_pattern =  "http://api.openweathermap.org/data/2.5/forecast?zip={},{}&appid={}"

    def __init__(self, zip_code=weather.shared.ZIP_CODE, country_code=weather.shared.COUNTRY_CODE, should_get_forcast=False):
        self.zip_code = zip_code
        self.country_code = country_code
        self.should_get_forcast = should_get_forcast
        self.appid = weather.shared.APP_KEY


    def __str__(self):
        if self.should_get_forcast:
            return self.forcast_pattern.format(self.zip_code, self.country_code, self.appid)
        return self.weather_pattern.format(self.zip_code,self.country_code,self.appid)

    def get_data(self):
        responseObject = json.loads(requests.get(str(self)).text)
        if self.should_get_forcast:
            return owmrf.OWMForcastResponse(responseObject)
        return owmr.OWMResponse(responseObject)
    