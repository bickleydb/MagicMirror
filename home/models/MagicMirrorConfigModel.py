from django.db import models
from django.utils.translation import gettext as _

from . import Name_Max_Length
from . import Unit_Max_Length
from . import CSS_Length_Units

class MagicMirrorConfigModel(models.Model):
    
    configurationName = models.CharField(max_length=Name_Max_Length,
            help_text=_("Friendly name to use to refer to this configuration")
    )

    startUpApp = models.ForeignKey("ApplicationDefinitionModel", 
        on_delete=models.CASCADE,
    )

    rows = models.IntegerField(_("Rows"),
             help_text=_("Number of rows to use in the main MagicMirror grid")
    )

    columns = models.IntegerField(_("Columns"),
            help_text = _("Number of columns to use in the main MagicMirror grid")
    )

    width_value = models.IntegerField(_("Width"),
            help_text= _("Number of whatever width unit desired")
    )
    
    width_unit = models.CharField(max_length=Unit_Max_Length,
            choices=CSS_Length_Units
    )

    height_value = models.IntegerField(_("Height"),
            help_text= _("Number of whatever column unit desired")
    )

    height_unit = models.CharField(max_length=Unit_Max_Length,
            choices=CSS_Length_Units
    )

    def __str__(self):
        return self.configurationName

    @staticmethod
    def get_manager():
        return MagicMirrorConfigModel.objects
    
    class Meta:
        verbose_name=_("Magic Mirror Configuration")
        verbose_name_plural = _("Magic Mirror Configurations")