# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=120)
    descripcion = models.CharField(max_length=300, null=True, blank=True)
    estado= models.BooleanField(default=True)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
    # end class

    def __unicode__(self):
        return u'%s %s' % (self.nombre)
    # end def

    def __str__(self):
        return u'%s %s' % (self.nombre)
    # end def
#end class


class UnidadNegocio(models.Model):
    nombre = models.CharField(max_length=120)
    descripcion = models.CharField(max_length=300, null=True, blank=True)
    estado= models.BooleanField(default=True)

    class Meta:
        verbose_name = "Unidad de negocio"
        verbose_name_plural = "Unidades de negocios"
    # end class

    def __unicode__(self):
        return u'%s %s' % (self.nombre)
    # end def

    def __str__(self):
        return u'%s %s' % (self.nombre)
    # end def
#end class


class Tipo(models.Model):
    nombre = models.CharField(max_length=120)
    descripcion = models.CharField(max_length=300, null=True, blank=True)
    estado= models.BooleanField(default=True)

    class Meta:
        verbose_name = "Tipo"
        verbose_name_plural = "Tipos"
    # end class

    def __unicode__(self):
        return u'%s %s' % (self.nombre)
    # end def

    def __str__(self):
        return u'%s %s' % (self.nombre)
    # end def
#end class



class Unidad(models.Model):
    nombre = models.CharField(max_length=120)
    descripcion = models.CharField(max_length=300, null=True, blank=True)
    estado= models.BooleanField(default=True)

    class Meta:
        verbose_name = "Unidad de negocio"
        verbose_name_plural = "Unidades de negocios"
    # end class

    def __unicode__(self):
        return u'%s %s' % (self.nombre)
    # end def

    def __str__(self):
        return u'%s %s' % (self.nombre)
    # end def
#end class


class Activo(models.Model):
    codigo = models.CharField(max_length=120, null=True, blank=True)
    nombre = models.CharField(max_length=120)
    descripcion = models.CharField(max_length=300, null=True, blank=True)
    presentacion = models.ForeignKey(Unidad)
    tipo = models.IntegerField(choices=((1,'Comercializar'),(1,'Compuesto'),(1,'Materia prima')))
    negocio = models.ForeignKey(UnidadNegocio)
    iva = models.BooleanField(default=False, verbose_name="Grabado con iva")
    ipoconsumo = models.BooleanField(default=False, verbose_name="Impoconsumo")
    precio_venta = models.FloatField(verbose_name='Precio de venta')
    adquisicion = models.FloatField(verbose_name='Precio de compra')
    rentabilidad = models.FloatField(verbose_name='Porcentaje de rentabilidad')
    rentabilidad_ingreso = models.FloatField(verbose_name='Porcentaje de rentabilidad sobre ingreso')

    class Meta:
        verbose_name = "Articulo"
        verbose_name_plural = "Articulos"
    # end class

    def __unicode__(self):
        return u'%s %s' % (self.nombre)
    # end def

    def __str__(self):
        return u'%s %s' % (self.nombre)
    # end def
#end class


class Salida(models.Model):
    activo = models.ForeignKey(Activo)
    cantidad = models.FloatField(default=0)
    valor = models.FloatField(default=0)
    realizacion = models.DateTimeField(auto_now_add=True)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Salida de articulo"
        verbose_name_plural = "Salidas de articulos"
    # end class

    def __unicode__(self):
        return u'%s %s' % (self.nombre)
    # end def

    def __str__(self):
        return u'%s %s' % (self.nombre)
    # end def
#end class


class Entrada(Salida):
    activo_e = models.ForeignKey(Activo)
    cantidad_e = models.FloatField(default=0)
    valor_e = models.FloatField(default=0)

    class Meta:
        verbose_name = "Entrada de articulo"
        verbose_name_plural = "Entradas de articulos"
    # end class

    def __unicode__(self):
        return u'%s %s' % (self.nombre)
    # end def

    def __str__(self):
        return u'%s %s' % (self.nombre)
    # end def
#end class


class ComposicionProducto(models.Model):
    producto = models.ForeignKey(Activo)
    desc = models.CharField(max_length=300, null=True, blank=True, verbose_name="Descripción")
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Descripción composicion de articulo"
        verbose_name_plural = "Entradas de articulos"
    # end class

    def __unicode__(self):
        return u'%s %s' % (self.producto.nombre)
    # end def

    def __str__(self):
        return u'%s %s' % (self.producto.nombre)
    # end def
#end class


class Descripcion(models.Model):
    composicion =models.ForeignKey(ComposicionProducto)
    articulo = models.ForeignKey(Activo, related_name='desc_art')
    cantidad = models.FloatField(default=0)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Descripción composicion de articulo"
        verbose_name_plural = "Entradas de articulos"
    # end class

    def __unicode__(self):
        return u'%s %s' % (self.nombre)
    # end def

    def __str__(self):
        return u'%s %s' % (self.nombre)
    # end def
