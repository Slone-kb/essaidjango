from django.urls import path
from django.contrib import admin
from . import views



urlpatterns=[

     path('', views.home_views, name='home'),
     path('about/', views.about_views, name='about'),
     path('contact/', views.contact_views, name='contact'),
     path('produits_details/<int:id>/', views.produits_details_views, name='produits_details'),
     path('produits_liste/', views.produits_liste_views, name='produits_liste'),
     # path('produits_create/', views.produits_forms_views, name='produits_forms')
     path('produits_create/', views.produits_create_views, name='produits_create')
     ]