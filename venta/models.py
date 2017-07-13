# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from cliente import models as cliente
from inventario import models as inventario
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Factura(models.Model):
    comprador = models.ForeignKey(cliente.Ciente, null=True, blank=True, related_name='comprador_factura')
    fecha = models.DateTimeField(default=timezone.now)
    subtotal = models.FloatField(default=0)
    iva = models.FloatField(default=0)
    impoconsumo = models.FloatField(default=0)
    total = models.FloatField(default=0)
    creador = models.ForeignKey(User, null=True, blank=True, related_name='creador_factura')
    paga = models.BooleanField(default=False)
    estado = models.BooleanField(default=True)
    pago = models.IntegerField(choices=((1,'Contado'),(2,'Credito')), verbose_name='Tipo de pago')

    def __unicode__(self):
        if self.comprador:
            return '%s %s' % (self.comprador.first_name, self.comprador.last_name)
        #end if
        return 'No cliente registrado para venta'
    # end def

    def __str__(self):
        if self.comprador:
            return '%s %s' % (self.comprador.first_name, self.comprador.last_name)
        #end if
        return 'No cliente registrado para venta'
    # end def

    class Meta:
        verbose_name = "Factura"
        verbose_name_plural = "Facturas"
    # end class
#end class


class Detalle(models.Model):
    factura = models.ForeignKey(Factura)
    articulo = models.ForeignKey(inventario.Activo)
    cantidad= models.FloatField(default=0)
    valor_unitario = models.FloatField(default=0)
    total = models.FloatField(default=0)

    def __unicode__(self):
        if self.factura.comprador:
            return '%s %s' % (self.factura.comprador.first_name, self.factura.comprador.last_name)
        #end if
        return 'No cliente registrado para venta'
    # end def

    def __str__(self):
        if self.factura.comprador:
            return '%s %s' % (self.factura.comprador.first_name, self.factura.comprador.last_name)
        #end if
        return 'No cliente registrado para venta'
    # end def

    class Meta:
        verbose_name = "Descripcion factura"
        verbose_name_plural = "Descripciones de Facturas"
    # end class
#end class
