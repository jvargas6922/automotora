from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView


def index(request):
    return render(request, 'index.html')



    
