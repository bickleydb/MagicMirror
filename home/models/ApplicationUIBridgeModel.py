from django.db import models
from django.utils.translation import gettext as _


class ApplicationUIBridgeModel(models.Model):

    app_help_text = _("Application to use with a particular UI configuration")
    ui_config_help_text = _("UI configuration for the app")

    app = models.ForeignKey("ApplicationDefinitionModel",
                            on_delete=models.CASCADE,
                            verbose_name=_("Application"),
                            help_text=app_help_text
                            )

    UI_Config = models.ForeignKey("ApplicationUIConfigModel",
                                  on_delete=models.CASCADE,
                                  verbose_name=_("Configuration"),
                                  help_text=ui_config_help_text
                                  )

    def __str__(self):
        return str(self.app) + " to " + str(self.UI_Config)

    @staticmethod
    def get_manager():
        return ApplicationUIBridgeModel.objects

    class Meta:
        verbose_name = _("App UI Bridge")
        verbose_name_plural = _("App UI Bridges")
