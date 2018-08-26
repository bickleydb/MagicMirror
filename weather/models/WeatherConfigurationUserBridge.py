from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _

class WeatherConfigurationUserBridge (models.Model):
    user = models.ForeignKey(User,
        on_delete=models.CASCADE
    )
    
    weatherConfiguration = models.ForeignKey('WeatherConfigurationModel',
        on_delete=models.CASCADE
    )

    def __str__(self): 
        return  self.user.username + " : " + str(self.weatherConfiguration)