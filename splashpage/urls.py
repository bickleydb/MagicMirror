from django.urls import path
import splashpage.views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',  splashpage.views.loadHTML, name="loadHTML"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
