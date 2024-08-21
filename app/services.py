from .models import *

#TIPO_USUARIOS
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

#TIPO_AUTOS    
def get_tipo_autos():
    return TipoAuto.objects.all()

def crear_tipo_auto(nombre):
    try:
        tipo = TipoAuto(
            tipo_auto=nombre
        )
        tipo.save()
        return tipo
    except Exception as e:
        return e
    
def tipo_auto(id):
    try:
        return TipoAuto.objects.get(id_tipo_auto=id)
    except Exception as e:
        return e
    
def actualiza_tipo_auto(id, nombre):
    try:
        tipo = tipo_auto(id)
        tipo.nombre = nombre
        tipo.save()
        return tipo
    except Exception as e:
        return e
    
def elimina_tipo_auto(id):
    try:
        tipo = tipo_auto(id)
        tipo.delete()
        return True
    except Exception as e:
        return e

#AUTOS
def get_autos():
    return Auto.objects.all()

def crear_auto(nro_asiento, anio, marca, nro_venta, precio, tipo_auto, comuna, usuario):
    try:
        auto = Auto(
            nro_asiento=nro_asiento,
            anio=anio,
            marca=marca,
            nro_venta=nro_venta,
            precio=precio,
            tipo_auto=tipo_auto,
            comuna=comuna,
            usuario=usuario
        )
        auto.save()
        return auto
    except Exception as e:
        return e

def auto(id):
    try:
        return Auto.objects.get(id_auto=id)
    except Exception as e:
        return e
    
def actualizar_auto(id, nro_asiento=None, anio=None, marca=None, nro_venta=None, precio=None, tipo_auto=None, comuna=None, usuario=None):
    try:
        auto = auto(id)
        if nro_asiento:
            auto.nro_asiento = nro_asiento
        if anio:
            auto.anio = anio
        if marca:
            auto.marca = marca
        if nro_venta:
            auto.nro_venta = nro_venta
        if precio:
            auto.precio = precio
        if tipo_auto:            
            auto.tipo_auto = tipo_auto
        if comuna:
            auto.comuna = comuna
        if usuario:
            auto.usuario = usuario
        auto.save()
        return auto
    except Exception as e:
        return e