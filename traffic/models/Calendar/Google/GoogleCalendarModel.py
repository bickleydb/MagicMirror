from django.db import models
from . import Name_Max_Length, Id_Max_Length


class GoogleCalendarModel(models.Model):
    calendar_name = models.CharField(max_length=Name_Max_Length)
    calendar_id = models.CharField(max_length=Id_Max_Length)

    def get_manager():
        return GoogleCalendarModel.objects

    def __str__(self):
        return self.calendar_name
