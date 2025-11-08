
from django.urls import path

from . import views

#localhost:8000/DJapp
urlpatterns = [  
    path('', views.all_dj, name = 'all_dj'),

] 
