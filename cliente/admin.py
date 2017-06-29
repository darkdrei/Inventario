# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
import forms
import models
# Register your models here.


class ClienteAdmin(admin.ModelAdmin):
    list_display = ['identificacion', 'email', 'first_name', 'last_name',
                    'direccion', 'telefono', 'nacimiento']
    search_fields = ['identificacion', 'email', 'first_name', 'last_name',
                    'direccion', 'telefono', 'nacimiento']
    icon = '<i class="material-icons">accessibility</i>'
    
    def get_form(self, request, obj=None, *args, **kwargs):
        if obj:
            kwargs['form'] = forms.ProveedorFormEdit
        # end if
        return super(ProveedorAdmin, self).get_form(request, obj, *args, **kwargs)
    # end def
#end class

admin.site.register(models.Ciente, ClienteAdmin)
