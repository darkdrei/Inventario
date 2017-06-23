# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
import models
import forms
from inventario import models as inventario
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

    def save_model(self, request, obj, form, change):
        obj.save()
        total = 0
        for s in models.Detalle.objects.filter(factura__id=obj.id):
            articulo = inventario.Activo.objects.filter(id=s.articulo.id).first()
            if s.cantidad > s.articulo.existencias :
                s.cantidad = s.articulo.existencias
            #end if
            if articulo:
                articulo.existencias = articulo.existencias - s.cantidad
                articulo.save()
                total = s.cantidad * articulo.precio_venta
            #end if
        # end for
        obj.total = total
        obj.save()
    # end if
#end class


class DetalleAdmin(admin.ModelAdmin):
    list_display = ['factura','articulo','cantidad','valor_unitario','total']
    search_fields = ['factura','articulo','cantidad','valor_unitario','total']
    form = forms.DetalleForm
#end class


admin.site.register(models.Factura, FacturaAdmin)
admin.site.register(models.Detalle, DetalleAdmin)
