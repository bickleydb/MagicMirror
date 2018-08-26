from django.db import models
from django.utils.translation import gettext as _

from . import CSS_Length_Units
from . import Name_Max_Length

class ApplicationUIConfigModel(models.Model):

    name = models.CharField(_("Name"), 
            max_length=Name_Max_Length,
            help_text=_("Friendly name to refer to this UI configuration.")
    )

    startRow = models.IntegerField(_("Start Row"), 
            help_text=_("The first row that this app should take up in the CSS Grid. Starts at 1")
    )

    endRow = models.IntegerField(_("End Row"),
             help_text=_("The last row that this app should take up in the CSS Grid. Exclusive")
    )
        
    startColumn = models.IntegerField(_("Start Column"),
            help_text=_("The first column that this app should take up in the CSS Grid. Starts at 1")
    )
    endColumn = models.IntegerField(_("End Column"),
            help_text=_("The last column that this app should take up in the CSS Grid. Exclusive")
    )

    startOnStartup = models.BooleanField(_("Should Load On Start"))
    
    @staticmethod
    def get_manager():
        return ApplicationUIConfigModel.objects

    def __str__(self):
        return self.name

    class Meta:
        verbose_name= _("App UI Configuration")
        verbose_name_plural = _("App UI Configurations")