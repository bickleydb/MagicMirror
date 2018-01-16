from django.contrib import admin
from .models.weather_models import daily_weather as dm
# Register your models here.
admin.site.register(dm)
