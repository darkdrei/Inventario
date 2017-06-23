from django.contrib.auth.forms import UserCreationForm
from django import forms
import models

class CompraForm(forms.ModelForm):
    class Meta:
        model = models.Compra
        fields = ['articulo','cantidad','valor_unitario','total','iva','valor_iva','aprobado']
        exclude = ['estado','paga','realizacion']
    #end class
#end class
