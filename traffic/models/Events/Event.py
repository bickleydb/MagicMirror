from django.db import models
from . import Name_Max_Length
from django.contrib.auth.models import User


class Event(models.Model):
    eventName = models.CharField(max_length=Name_Max_Length)
    startDateTime = models.DateTimeField(auto_now=False)
    endDateTime = models.DateTimeField(auto_now=False)
    location = models.ForeignKey('LocationModel', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
