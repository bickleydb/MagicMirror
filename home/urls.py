from django.urls import path
from home.views import views
urlpatterns = [
    path('startup/', views.load_html, name="load_html"),
    path('loadApplications', views.load_applications, name="load_applications"),
    path('loadApp/<str:appName>', views.load_app, name="load_app"),
    path('loadConfiguration', views.load_app_config, name="load_app_config"),
    path('loadDeviceData', views.load_device_data, name="load_device_data"),
    path('deviceLogin', views.login_by_device, name="login_by_device"),
    path('devicecreate', views.create_device, name="create_device"),
    path('', views.load_html, name="load_html")
]
