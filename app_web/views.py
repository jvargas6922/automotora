from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegistroForm()
    return render(request, 'registro/registro.html', {'form': form})

def CustomLoginView(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'registro/login.html', {'form': form})