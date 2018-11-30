from django.db import models

from . import Name_Max_Length

import uuid

class MultiAppModel(models.Model):
    readonly_fields  = ["uniqueId"]
    uniqueId = models.UUIDField("Unique ID", default = uuid.uuid4, unique=True, editable=False)
    name = models.CharField(max_length=Name_Max_Length)

    def __str__(self):
        return self.name

    @staticmethod
    def get_manager():
        return MultiAppModel.objects