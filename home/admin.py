from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models.ApplicationModel import ApplicationDefinition, Fonts, AppCSSFiles, CSSResources, MagicMirrorConfig
# Register your models here.
admin.site.register(ApplicationDefinition)
admin.site.register(AppCSSFiles)
admin.site.register(CSSResources)
admin.site.register(MagicMirrorConfig)
admin.site.register(Fonts)
