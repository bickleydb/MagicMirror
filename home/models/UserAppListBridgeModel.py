from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _

class UserAppListBridgeModel(models.Model):

    user = models.ForeignKey(User,
        on_delete=models.CASCADE
    )
    
    app = models.ForeignKey('ApplicationDefinitionModel',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.user.username + " : " + self.app.name

    @staticmethod
    def get_manager():
        return UserAppListBridgeModel.objects

    class Meta:
        verbose_name=_("User App List")
        verbose_name_plural = _("User App Lists")

