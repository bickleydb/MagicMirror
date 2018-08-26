from django.db import models
from django.utils.translation import gettext as _

class ApplicationCSSFileBridgeModel(models.Model):

    actualApp = models.ForeignKey("ApplicationDefinitionModel",
                                on_delete=models.CASCADE,
                                verbose_name=_("Application"),
                                help_text=_("Application you want to associate a CSS File with")
    )
    css_resource = models.ForeignKey("CSSResourceModel",
                                on_delete=models.CASCADE,
                                verbose_name=_("CSS File"),
                                help_text=_("CSS file to be loaded when the application is loaded")
    )

    def __str__(self):
        return self.actualApp.name +" : " + self.css_resource.sourcePath

    @staticmethod
    def get_manager():
        return ApplicationCSSFileBridgeModel.objects

    class Meta:
        verbose_name=_("App / CSS Bridge")
        verbose_name_plural = _("App / CSS Bridges")