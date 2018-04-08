from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import ApplicationCSSFileBridgeModel, ApplicationDefinitionModel, ApplicationUIBridgeModel,ApplicationUIConfigModel,CSSResourceModel,FontModel,MagicMirrorConfigModel

# Register your models here.
admin.site.register(ApplicationDefinitionModel.ApplicationDefinitionModel)
admin.site.register(ApplicationCSSFileBridgeModel.ApplicationCSSFileBridgeModel)
admin.site.register(CSSResourceModel.CSSResourceModel)
admin.site.register(MagicMirrorConfigModel.MagicMirrorConfigModel)
admin.site.register(FontModel.FontModel)
admin.site.register(ApplicationUIConfigModel.ApplicationUIConfigModel)
admin.site.register(ApplicationUIBridgeModel.ApplicationUIBridgeModel)