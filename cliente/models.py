# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from empleados import models as empleado

# Create your models here.
class Ciente(empleado.Persona):
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
    # end class
# end class
