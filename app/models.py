from django.db import models

# Create your models here.

class TipoUsuario(models.Model):
    id_tipo_usuario = models.AutoField(primary_key=True)
    tipo_usuario = models.CharField(max_length=50, null=False)

    class Meta:
        managed = False
        db_table = 'tipo_usuarios'

    def __str__(self):
        return self.tipo_usuario    

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, null=False)
    apellido = models.CharField(max_length=50, null=False)
    rut = models.CharField(max_length=12, null=False, unique=True)
    direccion = models.CharField(max_length=100, null=False)
    telefono = models.CharField(max_length=20, null=False)
    correo = models.EmailField(unique=True, null=False)
    tipo_usuario = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE, db_column='id_tipo_usuario')

    class Meta:
        managed = False
        db_table = 'usuarios'

    def __str__(self):
        return self.nombre

class Region(models.Model):
    id_region = models.AutoField(primary_key=True)
    region = models.CharField(max_length=200, null=False)

    class Meta:
        managed = False
        db_table = 'regiones'
    
    def __str__(self):
        return self.region
       
class Comuna(models.Model):
    id_comuna = models.AutoField(primary_key=True)
    comuna = models.CharField(max_length=200, null=False)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, db_column='id_region')

    class Meta:
        managed = False
        db_table = 'comunas'

    def __str__(self):
        return self.comuna

class TipoAuto(models.Model):
    id_tipo_auto = models.AutoField(primary_key=True)
    tipo_auto = models.CharField(max_length=200, null=False)

    class Meta:
        managed = False
        db_table = 'tipo_autos'

    def __str__(self):
        return self.tipo_auto

class Auto(models.Model):
    id_auto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200, null=False)
    nro_asiento = models.IntegerField(null=False)
    anio = models.IntegerField(null=False)
    marca = models.CharField(max_length=200, null=False)
    nro_venta = models.IntegerField(null=False)
    precio = models.IntegerField(null=False)
    tipo_auto = models.ForeignKey(TipoAuto, on_delete=models.CASCADE, db_column='id_tipo_auto')
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE, db_column='id_comuna')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, db_column='id_usuario')

    class Meta:
        managed = False
        db_table = 'autos'

    def __str__(self):
        return self.nombre



    
