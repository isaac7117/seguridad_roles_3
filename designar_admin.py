import os
import django

# Configura Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'seguridad_roles_3.settings')
django.setup()

from usuarios.models import Usuario

def designar_admin(username):
    try:
        usuario = Usuario.objects.get(username=username)
        usuario.rol = 'admin'  # Cambia 'admin' por el valor que hayas definido
        usuario.save()
        print(f"{username} ha sido designado como administrador.")
    except Usuario.DoesNotExist:
        print(f"El usuario {username} no existe.")

# Ejemplo de uso
designar_admin('Raul')