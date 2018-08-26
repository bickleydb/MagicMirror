from django.db import models
from django.utils.translation import gettext as _

from . import CSS_Length_Units
from . import Bundle_Path_Max_Length
from . import Name_Max_Length
from . import Unit_Max_Length

class ApplicationDefinitionModel(models.Model):

    name = models.CharField(
            _("Application Name"),
            max_length=Name_Max_Length,
            help_text=_("Friendly name to use to refer to this application.")
    )

    bundlePath = models.CharField(
        _("Javascript Bundle Name"),
        max_length=Bundle_Path_Max_Length,
        help_text=_("Location of the Javascript bundle that defines the app. Relative to the the /static/ endpoint")
    )

    width_value = models.IntegerField(_("Width"))
    
    width_unit = models.CharField(
        _("Width Units"),
        max_length=Unit_Max_Length,
        choices=CSS_Length_Units
    )

    height_value = models.IntegerField(_("Height"))

    height_unit = models.CharField(
        _("Height Units"),
        max_length=Unit_Max_Length,
        choices=CSS_Length_Units
    )

    hasCSS = models.BooleanField()
 
    @staticmethod
    def get_manager():
        return ApplicationDefinitionModel.objects

    def __str__(self):
        return self.name


    class Meta:
        verbose_name="Application Definition"
        verbose_name_plural = "Application Definitions"
