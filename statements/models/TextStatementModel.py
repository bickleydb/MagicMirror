from django.db import models


class TextStatementModel(models.Model):

    statement_text = models.CharField(max_length=500, blank=False, null = False)
    statement_author = models.CharField(max_length=500, blank=False, null=True)
    statement_source = models.ForeignKey('TextSatementSourceModel', on_delete=models.CASCADE, null=True)

    @staticmethod
    def get_manager():
        return TextStatementModel.objects

    def __str__(self):
        return str(self.statement_source) +" : " + self.statement_text