from django.contrib import admin

from traffic.models.LocationModel import LocationModel
from traffic.models.Path import Path

# Register your models here
admin.site.register(LocationModel)
admin.site.register(Path)