# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
import forms
import models
import nested_admin
from daterange_filter.filter import DateRangeFilter
# Register your models here.


class ProveedorAdmin(nested_admin.NestedModelAdmin):
    list_display = ('identificacion', 'email', 'first_name', 'last_name',
                    'direccion', 'telefono', 'nacimiento')
    list_filter =[('nacimiento', DateRangeFilter)]
    search_fields = (list_display)
    filter_horizontal = ('articulos',)
    form = forms.ProveedorForm
    icon = '<i class="material-icons">local_shipping</i>'

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

admin.site.register(models.Proveedor, ProveedorAdmin)
