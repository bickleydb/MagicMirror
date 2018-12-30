from django.db import models
from django.utils.translation import gettext as _
from . import Name_Max_Length


class PathLengthModel(models.Model):

    def seconds_name():
        return _("Expected duration in seconds")

    pathInstance = models.ForeignKey("Path",
                                     on_delete=models.CASCADE,
                                     verbose_name=_("Path Instance"),
                                     help_text=_("Relevant Path"))

    record_date = models.DateField(auto_now=True)
    record_time = models.TimeField(auto_now=True)
    secondsPerTrip = models.IntegerField(verbose_name=seconds_name())

    def get_manager():
        return PathLengthModel.objects

    def __str__(self):
        return "{} {} {}".format(
            self.pathInstance.PathName,
            str(self.record_date),
            str(self.record_time)
        )
