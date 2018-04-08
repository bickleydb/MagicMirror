from django.contrib import admin
from statements.models.TextStatementModel import TextStatementModel
from statements.models.TextStatementSourceModel import TextSatementSourceModel

# Register your models here.

admin.site.register(TextStatementModel)
admin.site.register(TextSatementSourceModel)
