from django.db import models
from django.utils.translation import gettext as _

from . import CSS_Length_Units
from . import Name_Max_Length


class ApplicationUIConfigModel(models.Model):

    name_help_text = _("Friendly name to refer to this UI configuration.")
    start_row_help_text = _("Starts at 1")
    end_row_help_text = _("Exclusive")
    start_col_help_text = _("Starts at 1")
    end_col_help_text = _("Exclusive")

    name = models.CharField(_("Name"),
                            max_length=Name_Max_Length,
                            help_text=name_help_text
                            )

    startRow = models.IntegerField(_("Start Row"), 
                                   help_text=start_row_help_text
                                   )

    endRow = models.IntegerField(_("End Row"),
                                 help_text=end_row_help_text
                                 )

    startColumn = models.IntegerField(_("Start Column"),
                                      help_text=start_col_help_text
                                      )

    endColumn = models.IntegerField(_("End Column"),
                                    help_text=end_col_help_text
                                    )

    startOnStartup = models.BooleanField(_("Should Load On Start"))

    @staticmethod
    def get_manager():
        return ApplicationUIConfigModel.objects

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("App UI Configuration")
        verbose_name_plural = _("App UI Configurations")
