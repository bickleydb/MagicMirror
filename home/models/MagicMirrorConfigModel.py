from django.db import models


class MagicMirrorConfigModel(models.Model):
    startUpApp = models.ForeignKey("ApplicationDefinitionModel", 
        on_delete=models.CASCADE,
    )
    rows = models.IntegerField("Rows")
    columns = models.IntegerField("Columns")
    width_value = models.IntegerField("Width")
    width_unit = models.CharField(max_length=10)
    height_value = models.IntegerField("Height")
    height_unit = models.CharField(max_length=10)

    @staticmethod
    def get_manager():
        return MagicMirrorConfigModel.objects
    
    class Meta:
        verbose_name="Magic Mirror Configuration"
        verbose_name_plural = "Magic Mirror Configurations"