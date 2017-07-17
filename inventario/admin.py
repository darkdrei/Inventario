# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
import models
import forms
# Register your models here.


class ActivoAdmin(admin.ModelAdmin):
    list_display= ['codigo','nombre','tipo','existencias','negocio','precio_venta','rentabilidad']
    search_fields =['codigo','nombre','descripcion','presentacion__nombre','negocio__nombre']
    list_filter=['negocio__nombre']
    form = forms.ArticuloForm
    icon = '<i class="material-icons">widgets</i>'

    def get_queryset(self, request):
        queryset = super(ActivoAdmin, self).get_queryset(request)
        return queryset
    #end def
#end class


class CategoriaAdmin(admin.ModelAdmin):
    list_display= ['nombre','descripcion','estado']
    search_fields = ['nombre','descripcion','estado']
    form = forms.CategoriaForm
    icon = '<i class="material-icons">label</i>'
#end class


class UnidadAdmin(admin.ModelAdmin):
    list_display= ['nombre','descripcion','estado']
    search_fields = ['nombre','descripcion','estado']
    form = forms.UnidadForm
    icon = '<i class="material-icons">widgets</i>'
#end class


class DescripcionInline(admin.StackedInline):
    model = models.Descripcion
    form = forms.DescripcionForm
    extra = 1
# end class


class ComposicionProductoAdmin(admin.ModelAdmin):
    list_display= ['producto','desc','estado']
    search_fields = ['producto','desc']
    form = forms.ComposicionProductoForm
    inlines = [DescripcionInline]
#end class


class UnidadAdmin(admin.ModelAdmin):
    list_display= ['nombre','descripcion','estado']
    search_fields = ['nombre','descripcion','estado']
    form = forms.UnidadForm
#end class


class SalidaAdmin(admin.ModelAdmin):
    list_display= ['activo','cantidad','valor', 'total','estado']
    search_fields = ['activo__nombre','estado']
    form = forms.SalidaForm
    icon = '<i class="material-icons">arrow_back</i>'

    def get_form(self, request, obj=None, *args, **kwargs):
        if obj:
            kwargs['form'] = forms.SalidaFormEdit
        # end if
        return super(EntredaAdmin, self).get_form(request, obj, *args, **kwargs)
    # end def
#end class


class EntredaAdmin(admin.ModelAdmin):
    list_display= ['activo','cantidad','cantidad_e', 'realizacion','estado']
    search_fields = ['activo','cantidad','valor','estado','total']
    form = forms.EntradaForm
    icon = '<i class="material-icons">arrow_forward</i>'

    def get_form(self, request, obj=None, *args, **kwargs):
        if obj:
            kwargs['form'] = forms.EntradaFormEdit
        # end if
        return super(EntredaAdmin, self).get_form(request, obj, *args, **kwargs)
    # end def
#end class


admin.site.register(models.Categoria, CategoriaAdmin)
admin.site.register(models.Tipo)
admin.site.register(models.Unidad, UnidadAdmin)
admin.site.register(models.Activo, ActivoAdmin)
admin.site.register(models.Salida, SalidaAdmin)
admin.site.register(models.Entrada, EntredaAdmin)
admin.site.register(models.ComposicionProducto, ComposicionProductoAdmin)
admin.site.register(models.Descripcion)
