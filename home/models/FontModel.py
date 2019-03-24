from django.db import models
from django.utils.translation import gettext as _
from . import Name_Max_Length
from . import Max_URL_Length


class FontModel(models.Model):
    name = models.CharField(
        _("Font Name"),
        max_length=Name_Max_Length,
        help_text=_("Friendly name to use to refer to this font")
    )

    url = models.CharField(
        _("Font URL"),
        max_length=Max_URL_Length,
        help_text=_("URL to use to load the font")
    )

    def __str__(self):
        return self.name

    @staticmethod
    def get_manager():
        return FontModel.objects

    class Meta:
        verbose_name = _("Font")
        verbose_name_plural = _("Fonts")
