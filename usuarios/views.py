from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UsuarioCreationForm
from .models import Usuario

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
            print(form.errors)  # Imprime los errores del formulario en la consola
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