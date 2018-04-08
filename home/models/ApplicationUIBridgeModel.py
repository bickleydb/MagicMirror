from django.db import models


class ApplicationUIBridgeModel(models.Model):
    app = models.ForeignKey("ApplicationDefinitionModel", on_delete=models.CASCADE, verbose_name="Application")
    UI_Config = models.ForeignKey("ApplicationUIConfigModel", on_delete=models.CASCADE, verbose_name="Configuration")

    def __str__(self):
        return str(self.app) + " to " + str(self.UI_Config)

    @staticmethod
    def get_manager():
        return ApplicationUIBridgeModel.objects

    class Meta:
        verbose_name="App UI Bridge"
        verbose_name_plural = "App UI Bridges"
