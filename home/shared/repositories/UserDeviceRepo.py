from home.models.UserDeviceBridge import UserDeviceBridge
from home.models.Device import DeviceModel


class UserDeviceRepo():

    def load_user_by_device_id(self, deviceId):
        bridgeManager = UserDeviceBridge.get_manager()
        deviceManager = DeviceModel.get_manager()
        device = deviceManager.get(deviceId=deviceId)
        instance = bridgeManager.get(device=device)
        return instance.user

    def load_user_by_device(self, device):
        manager = UserDeviceBridge.get_manager()
        instance = manager.get(device=device)
        return instance.user
