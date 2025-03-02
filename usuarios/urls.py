from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.registro, name='registro'),
    path('inicio/', views.inicio, name='inicio'),
    path('login/', views.inicio_sesion, name='login'),
]