from django import forms
import models
from material import *


class ArticuloForm(forms.ModelForm):
    class Meta:
        model = models.Activo
        fields = ['codigo','nombre','descripcion','presentacion','tipo','existencias','negocio','adquisicion','precio_venta','rentabilidad','rentabilidad_ingreso']
        exclude = ['estado']
        widgets = {
            'descripcion': forms.Textarea,
        }
    #end class

    def clean(self):
        data = super(ArticuloForm, self).clean()
        if data.get('existencias') :
            if data.get('existencias') <0:
                self.add_error('existencias', 'Debe por lo menos mantener existencias mayores iguales a cero.')
            #end if
        # end if
        if data.get('adquisicion') :
            if data.get('adquisicion') <0:
                self.add_error('adquisicion', 'Debe por lo menos ser mayor o igual a cero.')
            #end if
        # end if
        if data.get('precio_venta') :
            if data.get('precio_venta') <0:
                self.add_error('precio_venta', 'Debe por lo menos ser mayor o igual a cero.')
            #end if
        # end if
    # end def
#end class


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = models.Categoria
        fields = ['nombre','descripcion']
        exclude = ['estado']
        widgets = {
            'descripcion': forms.Textarea,
        }
    #end class
#end class


class UnidadForm(forms.ModelForm):
    class Meta:
        model = models.Unidad
        fields = ['nombre','descripcion']
        exclude = ['estado']
        widgets = {
            'descripcion': forms.Textarea,
        }
    #end class
#end class


class UnidadForm(forms.ModelForm):
    class Meta:
        model = models.Unidad
        fields = ['nombre','descripcion']
        exclude = ['estado']
        widgets = {
            'descripcion': forms.Textarea,
        }
    #end class
#end class


class SalidaForm(forms.ModelForm):
    class Meta:
        model = models.Salida
        fields = ['activo','cantidad']
        exclude = ['estado','total','realizacion','valor','total']
    #end class

    def clean(self):
        data = super(SalidaForm, self).clean()
        print 'este es el activo ************ ',data.get('activo').existencias
        if data.get('cantidad') :
            if data.get('cantidad') <0:
                self.add_error('cantidad', 'Debe por lo menos mantener existencias iguales a cero.')
            #end if
        # end if
        if data.get('cantidad') and data.get('activo'):
            if data.get('activo').existencias < data.get('cantidad'):
                self.add_error('cantidad', 'No debe rebasar las existencias q son %d.'%(data.get('activo').existencias))
            # end def
        # end if
    # end def

    def save(self, commit=True):
        cerrar = super(SalidaForm, self).save(commit)
        activo = models.Activo.objects.filter(id=cerrar.activo.id).first()
        activo.existencias = activo.existencias - cerrar.cantidad
        activo.save()
        cerrar.valor = activo.adquisicion
        cerrar.total = cerrar.cantidad * cerrar.valor
        cerrar.save()
        return cerrar
    # end def
#end class


class SalidaFormEdit(forms.ModelForm):
    class Meta:
        model = models.Salida
        fields = ['activo','cantidad']
        exclude = ['estado','total','realizacion','valor','total']
    #end class

    def clean(self):
        data = super(SalidaFormEdit, self).clean()
        if data.get('cantidad') :
            if data.get('cantidad') <0:
                self.add_error('cantidad', 'Debe por lo menos mantener existencias iguales a cero.')
            #end if
        # end if
        if data.get('cantidad') and data.get('activo'):
            if data.get('activo').existencias < data.get('cantidad'):
                self.add_error('cantidad', 'No debe rebasar las existencias q son %d.'%(data.get('activo').existencias))
            # end def
        # end if
    # end def
#end class


class EntradaForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(EntradaForm, self).__init__(*args, **kwargs)
        self.fields['activo'].label = "Articulo de salida"
        self.fields['cantidad'].label = "Cantidad de salida"
        self.fields['activo_e'].label = "Articulo de entrada"
        self.fields['cantidad_e'].label = "Cantidad de entrada"
    # end def

    class Meta:
        model = models.Entrada
        fields = ['activo','cantidad','activo_e','cantidad_e']
        exclude = ['estado','total',' realizacion','total_e','valor','valor_e']
        layout = Layout(Fieldset('Articulo de salida',
                             'activo', 'cantidad'),Fieldset('Articulo de entrada',
                                                  'activo_e', 'cantidad_e'))
    #end class

    def clean(self):
        data = super(EntradaForm, self).clean()
        print 'este es el activo ************ ',data.get('activo').existencias
        if data.get('cantidad') :
            if data.get('cantidad') <0:
                self.add_error('cantidad', 'Debe por lo menos mantener existencias iguales a cero.')
            #end if
        # end if
        if data.get('cantidad_e') :
            if data.get('cantidad_e') <0:
                self.add_error('cantidad_e', 'Debe por lo menos mantener existencias iguales a cero.')
            #end if
        # end if
        if data.get('cantidad') and data.get('activo'):
            if data.get('activo').existencias < data.get('cantidad'):
                self.add_error('cantidad', 'No debe rebasar las existencias q son %d.'%(data.get('activo').existencias))
            # end def
        # end if
    # end de

    def save(self, commit=True):
        cerrar = super(EntradaForm, self).save(commit)
        activo = models.Activo.objects.filter(id=cerrar.activo.id).first()
        activo.existencias = activo.existencias - cerrar.cantidad
        activo.save()
        activoe = models.Activo.objects.filter(id=cerrar.activo_e.id).first()
        activoe.existencias = activo.existencias + cerrar.cantidad_e
        activoe.save()
        cerrar.valor = activo.adquisicion
        cerrar.total = cerrar.cantidad * activo.adquisicion
        cerrar.valor_e = activoe.adquisicion
        cerrar.total_e = cerrar.cantidad_e * activoe.adquisicion
        cerrar.save()
        return cerrar
    # end def
#end class


class EntradaFormEdit(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(EntradaFormEdit, self).__init__(*args, **kwargs)
        self.fields['activo'].label = "Articulo de salida"
        self.fields['cantidad'].label = "Cantidad de salida"
        self.fields['activo_e'].label = "Articulo de entrada"
        self.fields['cantidad_e'].label = "Cantidad de entrada"
    # end def

    class Meta:
        model = models.Entrada
        fields = ['activo','cantidad','activo_e','cantidad_e']
        exclude = ['estado','total',' realizacion','total_e','valor','valor_e']
        widgets = {
            'cantidad': forms.TextInput(attrs={'readonly':'readonly'}),
            'cantidad_e': forms.TextInput(attrs={'readonly':'readonly'}),
        }
        layout = Layout(Fieldset('Articulo de salida',
                             'activo', 'cantidad'),Fieldset('Articulo de entrada',
                                                  'activo_e', 'cantidad_e'))
    #end class

    def clean(self):
        data = super(EntradaFormEdit, self).clean()
        if data.get('cantidad') :
            if data.get('cantidad') <0:
                self.add_error('cantidad', 'Debe por lo menos mantener existencias iguales a cero.')
            #end if
        # end if
        if data.get('cantidad_e') :
            if data.get('cantidad_e') <0:
                self.add_error('cantidad_e', 'Debe por lo menos mantener existencias iguales a cero.')
            #end if
        # end if
        if data.get('cantidad') and data.get('activo'):
            if data.get('activo').existencias < data.get('cantidad'):
                self.add_error('cantidad', 'No debe rebasar las existencias q son %d.'%(data.get('activo').existencias))
            # end def
        # end if
    # end de
#end class


class ComposicionProductoForm(forms.ModelForm):
    class Meta:
        model = models.ComposicionProducto
        fields = ['producto','desc','estado']
        exclude = []
        widgets = {
            'desc': forms.Textarea,
        }
    #end class

    def __init__(self, *args, **kwargs):
        super(ComposicionProductoForm, self).__init__(*args, **kwargs)
        self.fields['producto'].queryset = models.Activo.objects.filter(tipo=2)
    # end def
#end class


class DescripcionForm(forms.ModelForm):
    class Meta:
        model = models.Descripcion
        fields = ['composicion','articulo','cantidad']
        exclude = ['estado']
    #end class

    def __init__(self, *args, **kwargs):
        super(DescripcionForm, self).__init__(*args, **kwargs)
        self.fields['articulo'].queryset = models.Activo.objects.filter(tipo=3)
    # end def
#end class


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = models.Categoria
        fields = ['nombre','descripcion']
        exclude = ['estado']
        widgets = {
            'descripcion': forms.Textarea,
        }
    #end class
#end class
