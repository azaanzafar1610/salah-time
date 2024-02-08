from django.urls import path
from . import views

urlpatterns = [

    path('', views.main_prayer, name='main_prayer'),
    
    ]