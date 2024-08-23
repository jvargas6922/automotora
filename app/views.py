from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import *
from .models import *
from .services import *

# Create your views here.
def list_card(request):
    cars = get_autos()
    context ={ 'cars': cars }
    return render(request, 'car/index.html', context)

def create_car(request):
    if request.method == 'POST':
        form = AutoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Auto creado correctamente')
            return redirect('list_card')
        else:
            messages.warning(request, 'Error al crear auto')
    else:
        form = AutoForm()

    return render(request, 'car/create.html', {'form': form})


def register(request):
    if request.method == 'POST':
        #print(request.POST)
        result = crear_usuario(
            nombre=request.POST['first_name'],
            apellido=request.POST['last_name'],
            rut=request.POST['rut'],
            direccion=request.POST['direccion'],
            telefono=request.POST['telefono'],
            correo=request.POST['username'],
            tipo_usuario=1
        )
        if not result['success']:
            messages.warning(request, f"Error al crear usuario en la tabla personalizada: {result['error']}")
            return render(request, 'registration/register.html')
        
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username=username, password=password)
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            messages.success(request, 'Registro exitoso. Bienvenido!')
            return redirect('index')
        else:
            messages.error(request, 'Error en el registro.')
    return render(request, 'registration/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos')
    return render(request, 'portal_app/login.html')