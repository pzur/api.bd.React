# Generated by Django 3.0.2 on 2020-02-22 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('idcli', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=150)),
                ('apellido', models.CharField(max_length=150)),
                ('direccion', models.CharField(max_length=200)),
                ('telefono', models.IntegerField(blank=True, null=True)),
                ('correo', models.CharField(blank=True, max_length=200, null=True, unique=True)),
                ('usuario', models.CharField(blank=True, max_length=50, null=True)),
                ('pass_field', models.CharField(blank=True, db_column='pass', max_length=128, null=True)),
            ],
            options={
                'db_table': 'cliente',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ClienteMascota',
            fields=[
                ('idcl_mas', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'cliente_mascota',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Descripcion',
            fields=[
                ('iddes', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'descripcion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Detalle',
            fields=[
                ('iddet', models.AutoField(primary_key=True, serialize=False)),
                ('enfermedad', models.CharField(blank=True, max_length=150, null=True)),
                ('vacuna', models.CharField(blank=True, max_length=150, null=True)),
                ('alergia', models.CharField(blank=True, max_length=150, null=True)),
                ('observacion', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'detalle',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Disponibilidad',
            fields=[
                ('iddisp', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'disponibilidad',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Especialidad',
            fields=[
                ('idesp', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=150, null=True)),
            ],
            options={
                'db_table': 'especialidad',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('idhor', models.AutoField(primary_key=True, serialize=False)),
                ('hora', models.TimeField()),
                ('dia', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'horario',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('idmas', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
                ('raza', models.CharField(blank=True, max_length=50, null=True)),
                ('edad', models.IntegerField(blank=True, null=True)),
                ('peso', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('sexo', models.CharField(blank=True, max_length=50, null=True)),
                ('tipo_animal', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'mascota',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('idpago', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'pago',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Paseador',
            fields=[
                ('idpas', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=150)),
                ('apellido', models.CharField(max_length=150)),
                ('fecha_ingreso', models.DateTimeField(blank=True, null=True)),
                ('direccion', models.CharField(max_length=200)),
                ('telefono', models.IntegerField(blank=True, null=True)),
                ('correo', models.CharField(blank=True, max_length=200, null=True, unique=True)),
                ('dni', models.IntegerField(blank=True, null=True)),
                ('usuario', models.CharField(blank=True, max_length=150, null=True)),
                ('pass_field', models.CharField(blank=True, db_column='pass', max_length=128, null=True)),
                ('comentario', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'paseador',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('idprod', models.AutoField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(blank=True, max_length=50, null=True)),
                ('costo', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'producto',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Programacion',
            fields=[
                ('idprog', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'programacion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Promocion',
            fields=[
                ('idprom', models.AutoField(primary_key=True, serialize=False)),
                ('producto', models.CharField(blank=True, max_length=150, null=True)),
                ('fecha_inicio', models.DateTimeField(blank=True, null=True)),
                ('fecha_fin', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'promocion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('idres', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'reserva',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('idserv', models.AutoField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(blank=True, max_length=50, null=True)),
                ('costo', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'servicio',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TipoPago',
            fields=[
                ('idtip_pago', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'tipo_pago',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UsuarioCliente',
            fields=[
                ('idus_cli', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=150)),
                ('apellido', models.CharField(max_length=150)),
                ('usuario', models.CharField(blank=True, max_length=150, null=True)),
                ('correo', models.CharField(blank=True, max_length=200, null=True, unique=True)),
                ('contrasena', models.CharField(blank=True, max_length=128, null=True)),
                ('telefono', models.IntegerField(blank=True, null=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'usuario_cliente',
                'managed': False,
            },
        ),
    ]