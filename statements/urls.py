from django.urls import path
from django.conf import settings
from statements.views.StatementView import StatementView
from django.conf.urls.static import static

statementView = StatementView()

urlpatterns = [
    path('getValue/', statementView.get_random_value, name='get_random_value'),
    path('updateDB/', statementView.update_database, name='updateDatabase'),
    path('', statementView.index, name='index'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
