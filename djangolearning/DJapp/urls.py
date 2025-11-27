
from django.urls import path

from . import views

#localhost:8000/DJapp
urlpatterns = [  
    path('', views.all_dj, name = 'all_dj'),
    path('<int:anime_id>/', views.anime_detail, name = 'anime_detail'),
    path('stores_temp/', views.stores_view, name = 'stores_view'),
    
] 
