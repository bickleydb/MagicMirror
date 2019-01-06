from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import traffic.views as views


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
          name='RecalculatePathEstimate'),

     path('Calendar/GetCalendar',
          views.getCalendarById,
          name='getCalendarById'),

     path('Calendar/GetEvents',
          views.getEventsInCalendar,
          name='getEventsInCalendar'
          )

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
