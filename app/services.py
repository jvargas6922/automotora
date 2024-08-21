from .models import *

def get_tipo_usuarios():
    return TipoUsuario.objects.all()

def crear_tipo_usuario(nombre):
    try:
        tipo = TipoUsuario(
            tipo_usuario=nombre
        )
        tipo.save()
        return tipo
    except Exception as e:
        return e
    
def tipo_usuario(id):
    try:
        return TipoUsuario.objects.get(id_tipo_usuario=id)
    except Exception as e:
        return e

def actualiza_tipo_usuario(id, nombre):
    try:
        tipo = tipo_usuario(id)
        tipo.nombre = nombre
        tipo.save()
        return tipo
    except Exception as e:
        return e

def elimina_tipo_usuario(id):
    try:
        tipo = tipo_usuario(id)
        tipo.delete()
        return True
    except Exception as e:
        return e
