from django.db import models

class TextSatementSourceModel(models.Model):
    REDDIT = 'RE'
    TWITTER = 'TWI'
    SOURCE_CHOICES = (
        (REDDIT, "Reddit"),
        (TWITTER, "Twitter")
    )

    source_name = models.CharField(max_length=500, blank=False, null=False)
    source_site = models.CharField(max_length=10, choices=SOURCE_CHOICES, default=REDDIT)
    last_update_date_time = models.DateTimeField(blank=False)

    def get_manager():
        return TextSatementSourceModel.objects

    def __str__(self):
        if(self.source_site == 'TWI'):
             return "Twitter : " + self.source_name
        else:
            return "Reddit : " + self.source_name

    
    