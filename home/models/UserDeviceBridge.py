from django.db import models
from django.contrib.auth.models import User


class UserDeviceBridge(models.Model):

    user = models.ForeignKey(User,
                             on_delete=models.CASCADE
                             )

    device = models.ForeignKey("DeviceModel",
                               on_delete=models.CASCADE,
                               )

    @staticmethod
    def get_manager():
        return UserDeviceBridge.objects
