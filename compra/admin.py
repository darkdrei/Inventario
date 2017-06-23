# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
import models
import forms
# Register your models here.


class CompraAdmin(admin.ModelAdmin):
    list_display = ['articulo','cantidad','valor_unitario']
    search_fields = []
    form = forms.CompraForm
#end class


admin.site.register(models.Compra, CompraAdmin)
