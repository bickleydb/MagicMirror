
class OWMMainValues:
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