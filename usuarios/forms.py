from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class UsuarioCreationForm(UserCreationForm):
    class Meta:
        model = Usuario  # Usa tu modelo de usuario personalizado
        fields = ('username', 'email')  # Campos que quieres incluir en el formulario