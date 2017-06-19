# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
import models
import forms
# Register your models here.


class CompraAdmin(admin.ModelAdmin):
    list_display = ['proveedor', 'articulo','cantidad','valor_unitario']
    search_fields = ['proveedor__identificacion', 'proveedor__first_name','proveedor__last_name','articulo__codigo', 'articulo__nombre','cantidad','valor_unitario']
    form = forms.CompraForm
#end class


admin.site.register(models.Compra, CompraAdmin)
