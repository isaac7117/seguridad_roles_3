from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    rol = models.CharField(max_length=50, default='usuario')
    ROLES = (
        ('admin', 'Administrador'),
        ('editor', 'Editor'),
        ('usuario', 'Usuario'),
        
    )
    rol = models.CharField(max_length=20, choices=ROLES, default='usuario')