from django.db import models
from django.utils.translation import gettext as _

from . import Name_Max_Length

class Path(models.Model):
    
    PathName = models.CharField(
            max_length=Name_Max_Length,
            help_text=_("Friendly name to refer to this path.")
    )

    StartingLocation = models.ForeignKey("LocationModel",
                on_delete=models.CASCADE,
                verbose_name=_("Start Location"),
                related_name="starting_locations",
                help_text=_("Starting position of the path")
    )

    EndingLocation = models.ForeignKey("LocationModel",
                on_delete=models.CASCADE,
                related_name= "ending_locations",
                verbose_name=_("End Location"),
                help_text=_("Ending position of the path")
    )

    @staticmethod
    def get_manager():
        return Path.objects

    def __str__(self):
        return self.PathName