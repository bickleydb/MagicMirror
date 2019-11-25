import uuid
from django.db import models
from . import Name_Max_Length
from . import Unit_Max_Length
from . import CSS_Length_Units


class DeviceModel(models.Model):

    deviceId = models.UUIDField(primary_key=True,
                                default=uuid.uuid4,
                                editable=False)
    
    name = models.CharField(max_length=Name_Max_Length)

    width_value = models.IntegerField()

    width_unit = models.CharField(max_length=Unit_Max_Length,
                                  choices=CSS_Length_Units
                                  )

    height_value = models.IntegerField("Height")

    height_unit = models.CharField(max_length=Unit_Max_Length,
                                   choices=CSS_Length_Units
                                   )

    @staticmethod
    def to_dictionary(device):
        rtnVal = {}
        rtnVal["name"] = device.name
        rtnVal["id"] = device.pk.hex
        rtnVal["width_unit"] = device.width_unit
        rtnVal["width_value"] = device.width_value
        rtnVal["height_value"] = device.height_value
        rtnVal["height_unit"] = device.height_unit
        return rtnVal

    @staticmethod
    def from_dictionary(dictionary):
        responseVal = DeviceModel()
        if "name" in dictionary:
            responseVal.name = dictionary["name"],
        if "widthUnit" in dictionary:
            responseVal.width_unit = dictionary["widthUnit"]
        if "widthValue" in dictionary:
            responseVal.width_value = dictionary["widthValue"]
        if "heightValue" in dictionary:
            responseVal.height_value = dictionary["heightValue"]
        if "heightUnit" in dictionary:
            responseVal.height_unit = dictionary["heightUnit"]
        return responseVal

    @staticmethod
    def get_manager():
        return DeviceModel.objects
