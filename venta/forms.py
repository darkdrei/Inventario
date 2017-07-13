from django import forms
import models
from material import *
from inventario import models as inventario


class FacturaForm(forms.ModelForm):
    class Meta:
        model = models.Factura
        fields = ['comprador','fecha','subtotal','total','paga','pago','estado']
        exclude = []
    #end class

#end class


class DetalleForm(forms.ModelForm):
    class Meta:
        model = models.Detalle
        fields = ['factura','articulo','cantidad']
        exclude = ['estado','valor_unitario','total']
    #end class

    def __init__(self, *args, **kwargs):
        super(DetalleForm, self).__init__(*args, **kwargs)
        self.fields['articulo'].queryset = inventario.Activo.objects.filter(tipo__in=[1,2])
    # end def

    def clear(self):
        data = super(DetalleForm, self).clear()
        if data.get('cantidad'):
            if data.get('cantidad') < 0 :
                self.add_error('cantidad','La cantidad debe ser mayor o igual a cero.')
            #end if
        if data.get('articulo') and data.get('cantidad'):
            if data.get('articulo').existencias < data.get('cantidad'):
                self.add_error('cantidad','La cantidad debe ser mayor o igual a cero.')
            #end if
        #end if
    #end def
#end class
