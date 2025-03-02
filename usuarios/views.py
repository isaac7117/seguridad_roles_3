from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UsuarioCreationForm  # Importa el formulario personalizado
from .models import Usuario
from django.views.decorators.csrf import requires_csrf_token
from django.template import RequestContext


def registro(request):
    if request.method == 'POST':
        form = UsuarioCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.rol = 'usuario'  # Asigna un rol por defecto
            user.save()
            login(request, user)
            return redirect('inicio')
        else:
            print(form.errors)
    else:
        form = UsuarioCreationForm()
    return render(request, 'usuarios/registro.html', {'form': form})

def inicio_sesion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('inicio')
    return render(request, 'usuarios/login.html')

def inicio(request):
    return render(request, 'usuarios/inicio.html')


@requires_csrf_token
def csrf_failure_view(request, reason=""):
    return render(request, 'usuarios/csrf_failure.html', {'reason': reason})