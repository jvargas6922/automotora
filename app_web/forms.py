from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *

class RegistroForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['nombre','apellido','rut', 'direccion','telefono','correo','tipo_usuario','password1','password2']

class LoginForm(AuthenticationForm):
    username = forms.EmailField(label='Correo')