from .models import *
import logging

logger = logging.getLogger(__name__)

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
    
def obtener_tipo_usuario(id):
    try:
        return TipoUsuario.objects.get(id_tipo_usuario=id)
    except Exception as e:
        return e

def actualiza_tipo_usuario(id, nombre):
    try:
        tipo = obtener_tipo_usuario(id)
        tipo.nombre = nombre
        tipo.save()
        return tipo
    except Exception as e:
        return e

def elimina_tipo_usuario(id):
    try:
        tipo = obtener_tipo_usuario(id)
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
    
#REGIONES
def get_regiones():
    return Region.objects.all()

def crear_region(region):
    try:
        reg = Region(
            region=region
        )
        reg.save()
        return reg
    except Exception as e:
        return e

def region(id):
    try:
        return Region.objects.get(id_region=id)
    except Exception as e:
        return e

def actualiza_region(id, region):
    try:
        reg = region(id)
        reg.region = region
        reg.save()
        return reg
    except Exception as e:
        return e

def elimina_region(id):
    try:
        reg = region(id)
        reg.delete()
        return True
    except Exception as e:
        return e

#COMUNAS
def get_comunas():
    return Comuna.objects.all()

def crear_comuna(comuna, region):
    try:
        com = Comuna(
            comuna=comuna,
            region=region
        )
        com.save()
        return com
    except Exception as e:
        return e

def comuna(id):
    try:
        return Comuna.objects.get(id_comuna=id)
    except Exception as e:
        return e

def actualiza_comuna(id, comuna=None, region=None):
    try:
        com = comuna(id)
        if comuna:
            com.comuna = comuna
        if region:
            com.region = region
        com.save()
        return com
    except Exception as e:
        return e

def elimina_comuna(id):
    try:
        com = comuna(id)
        com.delete()
        return True
    except Exception as e:
        return e

#USUARIOS
def get_usuarios():
    return Usuario.objects.all()

def crear_usuario(nombre, apellido, rut, direccion, telefono,correo,tipo_usuario):
    try:
        tipo = obtener_tipo_usuario(tipo_usuario)
        user = Usuario(
            nombre=nombre,
            apellido=apellido,
            rut=rut,
            direccion=direccion,
            telefono=telefono,
            correo=correo,
            tipo_usuario=tipo
        )
        user.save()
        print(f"Usuario creado exitosamente: {user}")
        return {'success': True, 'user': user}
    except Exception as e:
        logger.error(f"Error al crear el usuario: {e}")
        print(f"Error al crear usuario: {e}")
        return {'success': False, 'error': str(e)}

def usuario(id):
    try:
        return Usuario.objects.get(id_usuario=id)
    except Exception as e:
        return e

def actualiza_usuario(
    id,
    nombre=None,
    apellido=None,
    rut=None,
    direccion=None,
    telefono=None,
    correo=None,
    tipo_usuario=None):
    try:
        user = usuario(id)
        if nombre:
            user.nombre = nombre
        if apellido:
            user.apellido = apellido
        if rut:
            user.rut = rut
        if direccion:
            user.direccion = direccion
        if telefono:
            user.telefono = telefono
        if correo:
            user.correo = correo
        if tipo_usuario:
            user.tipo_usuario = tipo_usuario
        user.save()
        return user
    except Exception as e:
        return e

def elimina_usuario(id):
    try:
        user = usuario(id)
        user.delete()
        return True
    except Exception as e:
        return e