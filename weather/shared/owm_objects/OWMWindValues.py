
class OWMWindValues:
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