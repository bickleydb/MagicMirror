from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static


urlpatterns = [
    path('getValue/', views.index, name='index'),
    path('getPath/', views.GetPath, name='GetPath'),

    path('getPathEstimate/',
         views.GetPathEstimate,
         name='GetPathEstimate'),

    path('RecordPathEstimate/',
         views.RecordPathEstimate,
         name='RecordPathEstimate'),

    path('RecalculatePathEstimate/',
         views.RecalculatePathEstimate,
         name='RecalculatePathEstimate')

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
