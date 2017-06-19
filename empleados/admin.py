# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
import models
import nested_admin
from daterange_filter.filter import DateRangeFilter
import forms
# Register your models here.


class ProveedorAdmin(nested_admin.NestedModelAdmin):
    list_display = ('identificacion', 'email', 'first_name', 'last_name',
                    'direccion', 'telefono', 'nacimiento')
    list_filter =[('nacimiento', DateRangeFilter)]
    search_fields = (list_display)
    filter_horizontal = ('articulos',)
    form = forms.ProveedorForm

    def get_form(self, request, obj=None, *args, **kwargs):
        if obj:
            kwargs['form'] = forms.ProveedorFormEdit
        # end if
        return super(ProveedorAdmin, self).get_form(request, obj, *args, **kwargs)
    # end def

    class Media:
        js = ('/static/empleados/js/empleados.js',)
    # end class
# end class


class CajeroAdmin(nested_admin.NestedModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name',
                    'direccion', 'telefono', 'nacimiento')
    search_fields = list_display
    form = forms.CajeroForm

    def get_form(self, request, obj=None, *args, **kwargs):
        if obj:
            kwargs['form'] = forms.CajeroFormEdit
        # end if
        return super(CajeroAdmin, self).get_form(request, obj, *args, **kwargs)
    # end def
# end class


class CajeroAdmin(nested_admin.NestedModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name',
                    'direccion', 'telefono', 'nacimiento')
    search_fields = list_display
    form = forms.CajeroForm

    def get_form(self, request, obj=None, *args, **kwargs):
        if obj:
            kwargs['form'] = forms.CajeroFormEdit
        # end if
        return super(CajeroAdmin, self).get_form(request, obj, *args, **kwargs)
    # end def
# end class


class AdministradorAdmin(nested_admin.NestedModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name',
                    'direccion', 'telefono', 'nacimiento')
    search_fields = list_display
    form = forms.AdministradorForm

    def get_form(self, request, obj=None, *args, **kwargs):
        if obj:
            kwargs['form'] = forms.AdministradorFormEdit
        # end if
        return super(CajeroAdmin, self).get_form(request, obj, *args, **kwargs)
    # end def
# end class


# Register your models here.
admin.site.register(models.Proveedor, ProveedorAdmin)
admin.site.register(models.Administrador, AdministradorAdmin)
admin.site.register(models.Cajero, CajeroAdmin)
