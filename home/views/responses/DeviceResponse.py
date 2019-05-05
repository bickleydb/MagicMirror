import json


class DeviceResponse():

    def __init__(self, deviceModel):
        self.model = deviceModel

    def to_json(self):
        return json.dumps({
            "id": str(self.model.deviceId),
            "name": self.model.name,
            "width_value": self.model.width_value,
            "width_unit": self.model.width_unit,
            "height_value": self.model.height_value,
            "height_unit": self.model.height_unit
        })