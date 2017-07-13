# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-12 21:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0003_auto_20170621_1900'),
    ]

    operations = [
        migrations.AddField(
            model_name='activo',
            name='minimo',
            field=models.FloatField(default=0, verbose_name='Stock minimo'),
        ),
        migrations.AlterField(
            model_name='activo',
            name='rentabilidad',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Porcentaje de rentabilidad'),
        ),
        migrations.AlterField(
            model_name='activo',
            name='rentabilidad_ingreso',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Porcentaje de rentabilidad sobre ingreso'),
        ),
    ]
