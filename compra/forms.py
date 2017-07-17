from django.contrib.auth.forms import UserCreationForm
from django import forms
import models
from django_select2.forms import (
    HeavySelect2MultipleWidget, HeavySelect2Widget, ModelSelect2MultipleWidget,
    ModelSelect2TagWidget, ModelSelect2Widget, Select2MultipleWidget,
    Select2Widget
)
from inventario import models as inventario

class CompraForm(forms.ModelForm):
    class Meta:
        model = models.Compra
        fields = ['proveedor','articulo','cantidad','valor_unitario']
        exclude = ['estado','paga','realizacion','iva','valor_iva','aprobado','total']
        widgets = {
            'proveedor': Select2Widget,
            'articulo': Select2Widget
        }
    #end class

    class Media:
        js = ['/static/compra/js/compra.js',]
    # end class

    def __init__(self, *args, **kwargs):
        super(CompraForm, self).__init__(*args, **kwargs)

    #end def

    def save(self, commit=True):
        compra = super(CompraForm, self).save(commit)
        articulo = inventario.Activo.objects.filter(id=compra.articulo.id).first()
        if articulo:
            total_inventatio = articulo.existencias * articulo.adquisicion
            total_compra = compra.cantidad * compra.valor_unitario
            compra.total =  total_compra
            articulo.adquisicion = (total_inventatio +total_compra)/(articulo.existencias + compra.cantidad)
            articulo.rentabilidad = articulo.precio_venta/articulo.adquisicion - 1
            articulo.existencias += compra.cantidad
            articulo.save()
            #https://es.porndoe.com/video/730709/colombiana-amateur-de-culo-respingon-recogida-follada-y-corrida-en-el-cono-1
            #https://es.porndoe.com/video/805261/la-culona-espanola-de-tetas-de-silicona-tania-follada-por-dos-tios-en-trio
        #end if
        compra.save()
        return compra
    #end def
#end class


class CompraFormEdit(forms.ModelForm):
    class Meta:
        model = models.Compra
        fields = ['proveedor','articulo','cantidad','valor_unitario']
        exclude = ['estado','paga','realizacion','iva','valor_iva','aprobado','total']
        widgets = {
            'proveedor': Select2Widget,
            'articulo': Select2Widget
        }
    #end class

    class Media:
        js = ['/static/compra/js/compra.js',]
    # end class

    def __init__(self, *args, **kwargs):
        super(CompraFormEdit, self).__init__(*args, **kwargs)
        print 'estos son los valores --> ',self.instance.cantidad,' -- ',self.instance.valor_unitario
        self.valores= [self.instance.cantidad,self.instance.valor_unitario]
    #end def

    def save(self, commit=True):
        compra = super(CompraFormEdit, self).save(commit)
        compra.save()
        return compra
    #end def
#end class
