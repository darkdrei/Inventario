# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-20 16:13
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import re


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120)),
                ('descripcion', models.CharField(blank=True, max_length=300, null=True)),
                ('estado', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Departamento',
                'verbose_name_plural': 'Departamentos',
            },
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('identificacion', models.CharField(max_length=20, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^([1-9]+[0-9]*){7,20}$'), 'No valida', 'invalid')])),
                ('direccion', models.CharField(max_length=300)),
                ('nacimiento', models.DateField(blank=True, null=True, verbose_name='Fecha de nacimiento')),
                ('telefono', models.CharField(blank=True, max_length=10, null=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='avatar')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='UnidadNegocio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120)),
                ('descripcion', models.CharField(blank=True, max_length=300, null=True)),
                ('estado', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Unidad de negocio',
                'verbose_name_plural': 'Unidades de negocios',
            },
        ),
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('persona_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='empleados.Persona')),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empleados.Departamento')),
            ],
            options={
                'verbose_name': 'Administrador',
                'verbose_name_plural': 'Administradores',
            },
            bases=('empleados.persona',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Cajero',
            fields=[
                ('persona_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='empleados.Persona')),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empleados.Departamento')),
            ],
            options={
                'verbose_name': 'Cajero',
                'verbose_name_plural': 'Cajeros',
            },
            bases=('empleados.persona',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('persona_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='empleados.Persona')),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empleados.Departamento')),
            ],
            options={
                'verbose_name': 'Trabajador',
                'verbose_name_plural': 'Trabajadores',
            },
            bases=('empleados.persona',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]