# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from empleados import models as empleado
from inventario import models as inventario

# Create your models here.


class Proveedor(empleado.Persona):
    articulos = models.ManyToManyField(inventario.Activo)

    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"
    # end class
# end class
