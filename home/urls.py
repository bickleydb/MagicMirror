from django.urls import path
from home.views import HomeViews, DeviceViews

urlpatterns = [
    path('startup/', HomeViews.load_html, name="load_html"),
    path('loadApplications', HomeViews.load_applications, name="load_applications"),
    path('loadApp/<str:appName>', HomeViews.load_app, name="load_app"),
    path('loadConfiguration', HomeViews.load_app_config, name="load_app_config"),
    path('loadDeviceData', DeviceViews.load_device_data, name="load_device_data"),
    path('deviceLogin/', DeviceViews.login_by_device, name="login_by_device"),
    path('devicecreate', DeviceViews.create_device, name="create_device"),
    path('', HomeViews.load_html, name="load_html")
]
