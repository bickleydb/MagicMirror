from django.urls import path
from home.views import views
urlpatterns = [
    path('startup/', views.loadHTML, name="loadHTML"),
    path('loadApplications', views.loadApplications, name="loadApplications"),
    path('loadApp/<str:appName>', views.loadApp, name="loadApp" ),
    path('loadConfiguration', views.loadAppConfig, name="LoadConfig"),
]