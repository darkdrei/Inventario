# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from empleados import models as empleado
from inventario import models as inventario
# Create your models here.


class Compra(models.Model):
    proveedor = models.ForeignKey(empleado.Proveedor)
    articulo = models.ForeignKey(inventario.Activo)
    cantidad = models.FloatField(default=0)
    valor_unitario = models.FloatField(default=0,verbose_name='Precio unitario')
    total = models.FloatField(default=0)
    realizacion = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    iva = models.BooleanField(default=False)
    valor_iva = models.FloatField(default=0)
    aprobado = models.BooleanField(default=False)
    paga = models.BooleanField(default=False)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Compra"
        verbose_name_plural = "Compras"
    # end class

    def __unicode__(self):
        return u'%s %s' % (self.nombre)
    # end def

    def __str__(self):
        return u'%s %s' % (self.nombre)
    # end def
#end class
