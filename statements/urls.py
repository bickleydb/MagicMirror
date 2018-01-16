from django.urls import path
from . import views

urlpatterns = [
    path('getValue/', views.get_random_value, name='get_random_value'),
    path('updateDB/', views.updateDatabase, name='updateDatabase'),
    path('', views.index, name='index'),
]