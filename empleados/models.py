# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import re
from django.core import validators
from django.contrib.auth.models import User

# Create your models
class UnidadNegocio(models.Model):
    nombre = models.CharField(max_length=120)
    descripcion = models.CharField(max_length=300, null=True, blank=True)
    estado= models.BooleanField(default=True)

    class Meta:
        verbose_name = "Unidad de negocio"
        verbose_name_plural = "Unidades de negocios"
    # end class

    def __unicode__(self):
        return u'%s' % (self.nombre)
    # end def

    def __str__(self):
        return u'%s' % (self.nombre)
    # end def
#end class


class Departamento(models.Model):
    nombre = models.CharField(max_length=120)
    descripcion = models.CharField(max_length=300, null=True, blank=True)
    estado= models.BooleanField(default=True)

    class Meta:
        verbose_name = "Departamento"
        verbose_name_plural = "Departamentos"
    # end class

    def __unicode__(self):
        return u'%s %s' % (self.nombre)
    # end def

    def __str__(self):
        return u'%s %s' % (self.nombre)
    # end def
#end class


class Persona(User):
    identificacion = models.CharField(max_length=20, unique=True, validators=[validators.RegexValidator(re.compile('^([1-9]+[0-9]*){7,20}$'), ('No valida'), 'invalid')])
    direccion = models.CharField(max_length=300, null=True, blank=True)
    nacimiento = models.DateField(verbose_name="Fecha de nacimiento", null=True,blank=True)
    telefono = models.CharField(max_length=10, null=True, blank=True)
    imagen = models.ImageField(upload_to="avatar", null=True, blank=True)

    def __unicode__(self):
        return '%s %s' % (self.last_name, self.first_name)
    # end def

    def __str__(self):
        return '%s %s' % (self.last_name, self.first_name)
    # end def
# end class


class Empleado(Persona):
    departamento = models.ForeignKey(Departamento,  null=True, blank=True)

    class Meta:
        verbose_name = "Trabajador"
        verbose_name_plural = "Trabajadores"
    # end class
# end class


class Cajero(Persona):
    negocio = models.ForeignKey(UnidadNegocio, verbose_name='Unidad de negocio')
    departamento = models.ForeignKey(Departamento,  null=True, blank=True)
    autenticate = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = "Cajero"
        verbose_name_plural = "Cajeros"
    # end class
# end class

class Administrador(Persona):
    departamento = models.ForeignKey(Departamento,  null=True, blank=True)

    class Meta:
        verbose_name = "Administrador"
        verbose_name_plural = "Administradores"
    # end class
# end class
