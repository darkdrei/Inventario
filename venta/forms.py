from django.contrib.auth.forms import UserCreationForm
from django import forms
import models

class FacturaForm(forms.ModelForm):
    class Meta:
        model = models.Factura
        fields = ['comprador','fecha','subtotal','iva','impoconsumo','total','creador','paga']
        exclude = ['estado']
    #end class
#end class


class DetalleForm(forms.ModelForm):
    class Meta:
        model = models.Detalle
        fields = ['factura','articulo','cantidad','valor_unitario','total']
        exclude = ['estado']
    #end class
#end class
