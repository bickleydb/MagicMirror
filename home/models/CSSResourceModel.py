from django.db import models


class CSSResourceModel(models.Model):
    sourcePath = models.CharField(max_length=255)
    
    def __str__(self):
        return self.sourcePath

    @staticmethod
    def get_manager():
        return CSSResourceModel.objects

    class Meta:
        verbose_name="CSS File"
        verbose_name_plural = "CSS Files"
