from django.db import models

class ApplicationCSSFileBridgeModel(models.Model):

    actualApp = models.ForeignKey("ApplicationDefinitionModel", on_delete=models.CASCADE, verbose_name="Application")
    css_resource = models.ForeignKey("CSSResourceModel", on_delete=models.CASCADE, verbose_name="CSS File")

    def __str__(self):
        return self.actualApp.name +" : " + self.css_resource.sourcePath

    @staticmethod
    def get_manager():
        return ApplicationCSSFileBridgeModel.objects

    class Meta:
        verbose_name="App / CSS Bridge"
        verbose_name_plural = "App / CSS Bridges"