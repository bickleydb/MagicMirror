from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static


urlpatterns = [
    path('loadAppDefs/', views.get_random_value, name='get_random_value'),
    path('updateDB/', views.updateDatabase, name='updateDatabase'),
    path('', views.index, name='index'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)