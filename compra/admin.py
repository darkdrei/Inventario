# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
import models
import forms
# Register your models here.


class CompraAdmin(admin.ModelAdmin):
    list_display = ['proveedor','articulo', 'cantidad', 'valor_unitario','total','realizacion']
    search_fields = []
    form = forms.CompraForm
    icon = '<i class="material-icons">shop</i>'

    def get_form(self, request, obj=None, *args, **kwargs):
        if obj:
            kwargs['form'] = forms.CompraFormEdit
        # end if
        return super(CompraAdmin, self).get_form(request, obj, *args, **kwargs)
    # end def
# end class


admin.site.register(models.Compra, CompraAdmin)
