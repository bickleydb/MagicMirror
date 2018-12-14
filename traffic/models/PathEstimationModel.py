from django.db import models
from django.utils.translation import gettext as _
from . import Name_Max_Length


class PathEstimationModel(models.Model):

    pathInstance = models.ForeignKey("Path",
                                     on_delete=models.CASCADE,
                                     verbose_name=_("Path Instance"),
                                     help_text=_("Relevant Path"))

    autoCompute = models.BooleanField("Autocompute?")
    expectedNumberSeconds = models.IntegerField(verbose_name=get_est_name())

    def get_est_name():
        return _("Best estimated guess for trip length")

    def get_manager():
        return PathEstimationModel.objects

    def __str__(self):
        return "{} : {} seconds".format(
            self.pathInstance.PathName,
            str(self.expectedNumberSeconds)
        )

