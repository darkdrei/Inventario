# -*- coding: utf-8 -*-
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from supra import views as supra
import models

# Create your views here.

class ListArtProveedor(supra.SupraListView):
    model = models.Activo
    list_display = ['id', 'nombre', 'codigo']
    search_key = 'q'
    list_filter = ['proveedor__id']
    search_fields = ['proveedor__id']

    def get_queryset(self):
        queryset = super(ListArtProveedor, self).get_queryset()
        obj = queryset.order_by('nombre')
        return obj
    # end def
# end class
