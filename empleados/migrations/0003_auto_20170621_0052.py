# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-21 00:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0002_auto_20170621_0015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administrador',
            name='departamento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='empleados.Departamento'),
        ),
        migrations.AlterField(
            model_name='cajero',
            name='departamento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='empleados.Departamento'),
        ),
    ]
