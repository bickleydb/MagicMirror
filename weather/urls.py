from django.urls import path
from django.conf import settings
from weather.views.WeatherView import WeatherView
from django.conf.urls.static import static

weatherView = WeatherView()

urlpatterns = [
    path('update', weatherView.update_today, name='update_today'),
    path('updateForcast', weatherView.update_forcast, name="update_forcast"),
    path('forcastView', weatherView.forcast_view, name="forcast_view"),
    path('force-update', weatherView.force_update, name="force_update"),
    path('', weatherView.index, name='index'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
