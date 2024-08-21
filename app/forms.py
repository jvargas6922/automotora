from django import forms
from .models import *
from django.contrib.auth import authenticate


class UsuarioForm(forms.ModelForm):
    class Meta:
        models = Usuario
        fields =[
            'nombre',
            'apellido',
            'rut',
            'direccion',
            'telefono',
            'correo',
            #'tipo_usuario'
        ]
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'rut': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            #'tipo_usuario': forms.Select(attrs={'class': 'form-control'}),
        }

class LoginForm(forms.ModelForm):
    correo_electronico = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean(self):
        cleaned_data = super().clean()
        correo_electronico = cleaned_data.get('correo_electronico')
        password = cleaned_data.get('password')
        user = authenticate(username=correo_electronico, password=password)
        if user is None:
            raise forms.ValidationError('Correo electrónico o contraseña incorrectos')
        return cleaned_data

    def get_user(self):
        correo_electronico = self.cleaned_data.get('correo_electronico')
        user = authenticate(username=correo_electronico, password=self.cleaned_data.get('password'))
        return user
    