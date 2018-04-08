from django.db import models

class FontModel(models.Model):
    name = models.CharField("Font Name", max_length=100)
    url = models.CharField("Font URL", max_length=1000)

    def __str__(self):
        return self.name
    
    @staticmethod
    def get_manager():
        return FontModel.objects

    class Meta:
        verbose_name="Font"
        verbose_name_plural = "Fonts"