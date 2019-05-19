from home.models.UserDeviceBridge import UserDeviceBridge
from home.models.Device import DeviceModel
import uuid


class UserDeviceRepo():

    def load_user_by_device_id(self, deviceId):
        bridgeManager = UserDeviceBridge.get_manager()
        deviceManager = DeviceModel.get_manager()
        searchId = uuid.UUID(deviceId)
        instance = bridgeManager.filter(device__deviceId=searchId)
        if not instance or not instance[0]:
            return None

        return instance[0].user

    def load_user_by_device(self, device):
        manager = UserDeviceBridge.get_manager()
        instance = manager.get(device=device)
        return instance.user
