# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-20 16:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.FloatField(default=0)),
                ('valor_unitario', models.FloatField(default=0, verbose_name='Precio unitario')),
                ('total', models.FloatField(default=0)),
                ('realizacion', models.DateTimeField(auto_now_add=True, null=True)),
                ('iva', models.BooleanField(default=False)),
                ('valor_iva', models.FloatField(default=0)),
                ('aprobado', models.BooleanField(default=False)),
                ('paga', models.BooleanField(default=False)),
                ('estado', models.BooleanField(default=True)),
                ('articulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.Activo')),
            ],
            options={
                'verbose_name': 'Compra',
                'verbose_name_plural': 'Compras',
            },
        ),
    ]
