from django.urls import path
from .views import registro, inicio_sesion, inicio

urlpatterns = [
path('registro/', registro, name='registro'),
path('login/', inicio_sesion, name='login'),
path('inicio/', inicio, name='inicio'),
]