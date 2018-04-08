from django.db import models

class ApplicationDefinitionModel(models.Model):
    name = models.CharField("Application Name", max_length=50)
    bundlePath = models.CharField("Javascript Bundle Name",max_length=100)
    hasCSS = models.BooleanField()
    width_value = models.IntegerField("Width")
    width_unit = models.CharField("Width Units", max_length=10)
    height_value = models.IntegerField("Height")
    height_unit = models.CharField("Height Units",max_length=10)
 
    @staticmethod
    def get_manager():
        return ApplicationDefinitionModel.objects

    def __str__(self):
        return self.name


    class Meta:
        verbose_name="Application Definition"
        verbose_name_plural = "Application Definitions"
