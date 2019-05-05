from django.db import models
from django.utils.translation import gettext as _
from . import Name_Max_Length


class Path(models.Model):

    def get_start_help_text():
        return _("Starting position of the path")

    def get_end_help_text():
        return _("Ending position of the path")

    PathName = models.CharField(
            max_length=Name_Max_Length,
            help_text=_("Friendly name to refer to this path.")
    )

    StartingLocation = models.ForeignKey("LocationModel",
                                         on_delete=models.CASCADE,
                                         verbose_name=_("Start Location"),
                                         related_name="starting_locations",
                                         help_text=get_start_help_text())

    EndingLocation = models.ForeignKey("LocationModel",
                                       on_delete=models.CASCADE,
                                       related_name="ending_locations",
                                       verbose_name=_("End Location"),
                                       help_text=get_end_help_text()
                                       )

    @staticmethod
    def get_manager():
        return Path.objects

    def __str__(self):
        return self.PathName
