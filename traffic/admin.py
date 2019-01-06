from django.contrib import admin

from traffic.models.LocationModel import LocationModel
from traffic.models.Path import Path
from traffic.models.PathEstimationModel import PathEstimationModel
from traffic.models.PathLengthModel import PathLengthModel
from traffic.models.Calendar.Google import GoogleCalendarModel
from traffic.models.Events import Event


class LocationAdmin(admin.ModelAdmin):
    readonly_fields = ('uniqueId',)

# Register your models here
admin.site.register(LocationModel, LocationAdmin)
admin.site.register(Path)
admin.site.register(PathLengthModel)
admin.site.register(PathEstimationModel)
admin.site.register(GoogleCalendarModel.GoogleCalendarModel)
admin.site.register(Event.Event)
