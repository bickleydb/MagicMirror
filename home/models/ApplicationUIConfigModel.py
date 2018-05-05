from django.db import models

class ApplicationUIConfigModel(models.Model):

    startRow = models.IntegerField("Start Row")
    endRow = models.IntegerField("End Row")
    startColumn = models.IntegerField("Start Column")
    endColumn = models.IntegerField("End Column")
    name = models.CharField("Name", max_length=100)
    startOnStartup = models.BooleanField("Should Load On Start")
    
    @staticmethod
    def get_manager():
        return ApplicationUIConfigModel.objects

    def __str__(self):
        return self.name

    class Meta:
        verbose_name="App UI Configuration"
        verbose_name_plural = "App UI Configurations"