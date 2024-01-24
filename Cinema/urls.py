from django.contrib import admin
from django.urls import path
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cennik/', views.cennik, name='cennik'),
    path('contact/', views.contact, name='contact'),
    path('details/<int:pk>/', views.details, name='details'),
    path('kup_bilet/', views.kup_bilet, name='kup_bilet'),
    path('kup_bilet/sukces/', views.kup_bilet_sukces, name='kup_bilet_sukces')
]