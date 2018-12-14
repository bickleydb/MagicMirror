class OWMSunValues:
    def __init__(self, sunrise_time=0, sunset_time=0):
        self.sunrise = sunrise_time
        self.sunset = sunset_time

    def get_sunrise_time(self):
        return self.sunrise

    def get_sunset_time(self):
        return self.sunset
