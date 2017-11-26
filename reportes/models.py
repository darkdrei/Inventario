# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class UnidadNedocio(models.Model):
    inicio = models.DateField(auto_now_add=True)
    fin = models.DateField(auto_now_add=True)

    def __unicode__(self):
        i = 0
        men = ''
        while i < 10 - len(str(self.instance.pk)):
            men = men + '0'
            i = i+1
        # end ford
        t = '%s%d' % (str(men), self.instance.pk)
        print t
        return u'%s' % (t)
    #end def

    def __str__(self):
        i = 0
        men = ''
        while i < 10 - len(str(self.instance.pk)):
            men = men + '0'
            i = i+1
        # end ford
        t = '%s%d' % (str(men), self.instance.pk)
        print t
        return u'%s' % (t)
    #end def

    class Meta:
        verbose_name = "Reporte unidad de negocio"
        verbose_name = "Reporte de unidades de negocios"
    #end class
