from django.db import models

from django.contrib.auth.models import User

class UserAppListBridgeModel(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    app = models.ForeignKey('ApplicationDefinitionModel', on_delete=models.CASCADE)


    @staticmethod
    def get_manager():
        return UserAppListBridgeModel.objects

    class Meta:
        verbose_name="User App List"
        verbose_name_plural = "User App Lists"

