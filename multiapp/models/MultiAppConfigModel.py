from django.db import models
from django.utils.translation import gettext as _

class MultiAppConfigModel(models.Model):

    pathInstance = models.ForeignKey("MultiAppModel",
                on_delete=models.CASCADE,
                verbose_name=_("MultiApp"),
                help_text=_("Relevant Model")
    )

    childApp = models.ForeignKey("home.ApplicationDefinitionModel",
        on_delete=models.CASCADE,
        verbose_name=_("Child apps"),
        help_text=_("Relevant apps")
    )

    @staticmethod
    def get_manager():
        return MultiAppConfigModel.objects