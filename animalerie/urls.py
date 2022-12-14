from django.urls import path, include
from . import views
from django.contrib import admin 
from django.conf import settings 
from django.conf.urls.static import static 

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('equipement', views.equipement_list, name='equipement_list'),
    path('animal/<str:pk>/', views.animal_detail, name='animal_detail'),
    path('ajout', views.ajout_animal, name = 'ajout_animal'), 
]