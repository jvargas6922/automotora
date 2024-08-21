from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .forms import *
from django.contrib import messages
from .models import *
from django.contrib.auth.models import User

# Create your views here.
def list_card(request):
    
    return render(request, 'car/index.html')

def register(request):
    if request.method == 'POST':
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