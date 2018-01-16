from django.db import models

class single_text_statement(models.Model):

    def get_manager():
        return single_text_statement.objects

    statement_text = models.CharField(max_length=500, blank=False, null = False)
    statement_author = models.CharField(max_length=500, blank=False, null=True)
    statement_source = models.ForeignKey('text_statement_source', on_delete=models.CASCADE, null=True)

   

class text_statement_source(models.Model):
    REDDIT = 'RE'
    TWITTER = 'TWI'
    SOURCE_CHOICES = (
        (REDDIT, "Reddit"),
        (TWITTER, "Twitter")
    )

    def get_manager():
        return text_statement_source.objects


    source_name = models.CharField(max_length=500, blank=False, null=False)
    source_site = models.CharField(max_length=10, choices=SOURCE_CHOICES, default=REDDIT)
    last_update_date_time = models.DateTimeField(blank=False)
    