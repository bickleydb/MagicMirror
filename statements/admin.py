from django.contrib import admin
from .models.statement_models import single_text_statement, text_statement_source
# Register your models here.
admin.site.register(single_text_statement)
admin.site.register(text_statement_source)
