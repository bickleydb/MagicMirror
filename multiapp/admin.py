from django.contrib import admin

from multiapp.models import MultiAppModel
from multiapp.models import MultiAppConfigModel

admin.site.register(MultiAppModel.MultiAppModel)
admin.site.register(MultiAppConfigModel.MultiAppConfigModel)
