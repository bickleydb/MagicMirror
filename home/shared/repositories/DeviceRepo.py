import home.models.Device as Devices
import uuid


class DeviceRepo:

    def save_new_device(self, deviceInfo):
        deviceInfo.save()

    def load_device_info(self, id):
        try:
            searchId = uuid.UUID(id)
            device = Devices.DeviceModel.get_manager().get(deviceId=searchId)
            return device
        except Exception as ex:
            print(ex)
            return None
