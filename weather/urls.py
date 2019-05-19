from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('update', views.update_today, name='update_today'),
    path('updateForcast', views.update_forcast, name="update_forcast"),
    path('forcastView', views.forcast_view, name="forcast_view"),
    path('', views.index, name='index'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
