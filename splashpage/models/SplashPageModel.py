from django.db import models

class SplashPageModel(models.Model):

    SplashPageName = models.CharField(max_length=20)
    SVGField = models.TextField()
    UseAnimation = models.BooleanField()
    BackgroundColorString = models.CharField(max_length=200)

    @staticmethod
    def get_manager():
        return SplashPageModel.objects

    def __str__(self):
        return self.SplashPageName

    class Meta:
        verbose_name="Splash Page"
        verbose_name_plural = "Splash Page"
