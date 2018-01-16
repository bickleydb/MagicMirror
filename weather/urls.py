from django.urls import path
from . import views

urlpatterns = [
    path('update', views.update_today, name='update_today' ),
    path('', views.index, name='index'),
]