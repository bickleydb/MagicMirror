from django.contrib import admin

from traffic.models.LocationModel import LocationModel
from traffic.models.Path import Path
from traffic.models.PathEstimationModel import PathEstimationModel
from traffic.models.PathLengthModel import PathLengthModel

class LocationAdmin(admin.ModelAdmin):
    readonly_fields = ('uniqueId',)

# Register your models here
admin.site.register(LocationModel, LocationAdmin)
admin.site.register(Path)
admin.site.register(PathLengthModel)
admin.site.register(PathEstimationModel)

