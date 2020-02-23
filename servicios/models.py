# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cliente(models.Model):
    idcli = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150)
    apellido = models.CharField(max_length=150)
    direccion = models.CharField(max_length=200)
    telefono = models.IntegerField(blank=True, null=True)
    correo = models.CharField(unique=True, max_length=200, blank=True, null=True)
    usuario = models.CharField(max_length=50, blank=True, null=True)
    pass_field = models.CharField(db_column='pass', max_length=128, blank=True, null=True)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = True
        db_table = 'cliente'

    def __str__(self):
        return self.nombre


class ClienteMascota(models.Model):
    idcl_mas = models.AutoField(primary_key=True)
    idcli = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='idcli', blank=True, null=True)
    idmas = models.ForeignKey('Mascota', models.DO_NOTHING, db_column='idmas', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cliente_mascota'


class Descripcion(models.Model):
    iddes = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    idserv = models.ForeignKey('Servicio', models.DO_NOTHING, db_column='idserv', blank=True, null=True)
    idprod = models.ForeignKey('Producto', models.DO_NOTHING, db_column='idprod', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'descripcion'


class Detalle(models.Model):
    iddet = models.AutoField(primary_key=True)
    enfermedad = models.CharField(max_length=150, blank=True, null=True)
    vacuna = models.CharField(max_length=150, blank=True, null=True)
    alergia = models.CharField(max_length=150, blank=True, null=True)
    observacion = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detalle'


class Disponibilidad(models.Model):
    iddisp = models.AutoField(primary_key=True)
    idhor = models.ForeignKey('Horario', models.DO_NOTHING, db_column='idhor', blank=True, null=True)
    idpas = models.ForeignKey('Paseador', models.DO_NOTHING, db_column='idpas', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'disponibilidad'


class Especialidad(models.Model):
    idesp = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'especialidad'


class Horario(models.Model):
    idhor = models.AutoField(primary_key=True)
    hora = models.TimeField()
    dia = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'horario'


class Mascota(models.Model):
    idmas = models.AutoField(primary_key=True)
    iddet = models.ForeignKey(Detalle, models.DO_NOTHING, db_column='iddet', blank=True, null=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    raza = models.CharField(max_length=50, blank=True, null=True)
    edad = models.IntegerField(blank=True, null=True)
    peso = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    sexo = models.CharField(max_length=50, blank=True, null=True)
    tipo_animal = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mascota'


class Pago(models.Model):
    idpago = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    idtip_pago = models.ForeignKey('TipoPago', models.DO_NOTHING, db_column='idtip_pago', blank=True, null=True)
    iddes = models.ForeignKey(Descripcion, models.DO_NOTHING, db_column='iddes', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pago'


class Paseador(models.Model):
    idpas = models.AutoField(primary_key=True)
    idesp = models.ForeignKey(Especialidad, models.DO_NOTHING, db_column='idesp', blank=True, null=True)
    nombre = models.CharField(max_length=150)
    apellido = models.CharField(max_length=150)
    fecha_ingreso = models.DateTimeField(blank=True, null=True)
    direccion = models.CharField(max_length=200)
    telefono = models.IntegerField(blank=True, null=True)
    correo = models.CharField(unique=True, max_length=200, blank=True, null=True)
    dni = models.IntegerField(blank=True, null=True)
    usuario = models.CharField(max_length=150, blank=True, null=True)
    pass_field = models.CharField(db_column='pass', max_length=128, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    comentario = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'paseador'


class Producto(models.Model):
    idprod = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=50, blank=True, null=True)
    costo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'producto'


class Programacion(models.Model):
    idprog = models.AutoField(primary_key=True)
    iddisp = models.ForeignKey(Disponibilidad, models.DO_NOTHING, db_column='iddisp', blank=True, null=True)
    idcl_mas = models.ForeignKey(ClienteMascota, models.DO_NOTHING, db_column='idcl_mas', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'programacion'


class Promocion(models.Model):
    idprom = models.AutoField(primary_key=True)
    producto = models.CharField(max_length=150, blank=True, null=True)
    fecha_inicio = models.DateTimeField(blank=True, null=True)
    fecha_fin = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'promocion'


class Reserva(models.Model):
    idres = models.AutoField(primary_key=True)
    idprog = models.ForeignKey(Programacion, models.DO_NOTHING, db_column='idprog', blank=True, null=True)
    idpago = models.ForeignKey(Pago, models.DO_NOTHING, db_column='idpago', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reserva'


class Servicio(models.Model):
    idserv = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=50, blank=True, null=True)
    costo = models.IntegerField(blank=True, null=True)
    idprom = models.ForeignKey(Promocion, models.DO_NOTHING, db_column='idprom', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'servicio'


class TipoPago(models.Model):
    idtip_pago = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_pago'


class UsuarioCliente(models.Model):
    idus_cli = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150)
    apellido = models.CharField(max_length=150)
    usuario = models.CharField(max_length=150, blank=True, null=True)
    correo = models.CharField(unique=True, max_length=200, blank=True, null=True)
    contrasena = models.CharField(max_length=128, blank=True, null=True)
    telefono = models.IntegerField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario_cliente'
