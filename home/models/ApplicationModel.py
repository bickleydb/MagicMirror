from django.db import models

class ApplicationDefinition(models.Model):
    name = models.CharField("Application Name", max_length=50)
    bundlePath = models.CharField("Javascript Bundle Name",max_length=100)
    hasCSS = models.BooleanField()
    width_value = models.IntegerField("Width")
    width_unit = models.CharField("Width Units", max_length=10)
    height_value = models.IntegerField("Height")
    height_unit = models.CharField("Height Units",max_length=10)
 
    def get_manager():
        return ApplicationDefinition.objects

    def __str__(self):
        return self.name


    class Meta:
        verbose_name="application definition"
        verbose_name_plural = "application definitions"

class Fonts(models.Model):
    name = models.CharField("Font Name", max_length=100)
    url = models.CharField("Font URL", max_length=1000)

    def __str__(self):
        return self.name
    
    def get_manager():
        return Fonts.objects

class AppCSSFiles(models.Model):
    actualApp = models.ForeignKey("ApplicationDefinition", on_delete=models.CASCADE, verbose_name="Application")
    css_resource = models.ForeignKey("CSSResources", on_delete=models.CASCADE, verbose_name="CSS File")

    def __str__(self):
        return self.actualApp.name +" : " + self.css_resource.sourcePath
    def get_manager():
        return AppCSSFiles.objects

class CSSResources(models.Model):
    sourcePath = models.CharField(max_length=255)
    
    def __str__(self):
        return self.sourcePath

    def get_manager():
        return CSSResources.objects

class MagicMirrorConfig(models.Model):
    startUpApp = models.ForeignKey("ApplicationDefinition", 
        on_delete=models.CASCADE,
    )
    
    def get_manager():
        return MagicMirrorConfig.objects

