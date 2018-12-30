from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import User


class PhoneNumberModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phoneNumber = models.CharField(max_length=12)

    def __str__(self):
        return "{} : {}".format(
            self.user.username,
            self.phoneNumber
        )

    class Meta:
        app_label = 'auth'
