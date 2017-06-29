# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
import models
import nested_admin
from daterange_filter.filter import DateRangeFilter
import forms
# Register your models here.


class UnidadNegocioAdmin(admin.ModelAdmin):
    list_display= ['nombre','descripcion','estado']
    search_fields = ['nombre','descripcion','estado']
    form = forms.UnidadNegocioForm
    icon = '<i class="material-icons">local_atm</i>'
#end class


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
    list_display = ('username', 'email', 'first_name', 'last_name','negocio',
                    'direccion', 'telefono', 'nacimiento')
    search_fields = ('username', 'email', 'first_name', 'last_name','negocio__nombre',
                    'direccion', 'telefono', 'nacimiento')
    form = forms.CajeroForm
    icon = '<i class="material-icons">account_box</i>'

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
    icon = '<i class="material-icons">account_circle</i>'

    def get_form(self, request, obj=None, *args, **kwargs):
        if obj:
            kwargs['form'] = forms.AdministradorFormEdit
        # end if
        return super(CajeroAdmin, self).get_form(request, obj, *args, **kwargs)
    # end def
# end class


# Register your models here.
admin.site.register(models.Administrador, AdministradorAdmin)
admin.site.register(models.Cajero, CajeroAdmin)
admin.site.register(models.UnidadNegocio, UnidadNegocioAdmin)
