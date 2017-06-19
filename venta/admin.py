# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
import models
import forms
# Register your models here.

class DetalleInline(admin.StackedInline):
    model = models.Detalle
    form = forms.DetalleForm
    extra = 1
# end class

class FacturaAdmin(admin.ModelAdmin):
    list_display = ['comprador','fecha','subtotal','iva','impoconsumo','total','creador','paga']
    search_fields = ['comprador','fecha','subtotal','iva','impoconsumo','total','creador','paga']
    form = forms.FacturaForm
    inlines = [DetalleInline,]
#end class


class DetalleAdmin(admin.ModelAdmin):
    list_display = ['factura','articulo','cantidad','valor_unitario','total']
    search_fields = ['factura','articulo','cantidad','valor_unitario','total']
    form = forms.DetalleForm
#end class


admin.site.register(models.Factura, FacturaAdmin)
admin.site.register(models.Detalle, DetalleAdmin)
