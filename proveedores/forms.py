# -*- coding: utf-8 -*-
from django.contrib.auth.forms import UserCreationForm
from django import forms
from exileui.widgets import DatePickerWidget
import models
from django.contrib.admin import widgets


class ProveedorForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(ProveedorForm, self).__init__(*args, **kwargs)
        self.fields['password1'].label = "Contraseña"
        self.fields['password2'].label = "Confirmar contraseña"
        self.fields['email'].label = "Correo Electrtónico"
        self.fields['first_name'].label = "Nombre"
        self.fields['nacimiento'].widget = DatePickerWidget(
            attrs={'class': 'dateopera'},
            format="%d/%m/%Y")
        self.fields['telefono'].widget = forms.NumberInput()
    # end def

    class Media:
        js = ('/static/empleados/js/dateoperario.js',)
    # end class

    class Meta:
        model = models.Proveedor
        fields = ['username', 'password1', 'password2', 'email', 'first_name',
                  'last_name', 'identificacion', 'direccion', 'telefono', 'nacimiento', 'imagen','articulos']
    # end class

    def save(self, commit=True):
        operario = super(ProveedorForm, self).save(commit)
        operario.is_staff = True
        operario.is_superuser = True
        operario.save()
        return operario
    # end def
# end class


class ProveedorFormEdit(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProveedorFormEdit, self).__init__(*args, **kwargs)
        self.fields['email'].label = "Correo Electrtónico"
        self.fields['first_name'].label = "Nombre"
        self.fields['last_name'].label = "Apellidos"
        self.fields['nacimiento'].widget = DatePickerWidget(
            attrs={'class': 'dateopera'},
            format="%d/%m/%Y")
        self.fields['telefono'].widget = forms.NumberInput()
    # end def

    class Media:
        js = ('/static/empleados/js/dateoperario.js',)
    # end class

    class Meta:
        model = models.Proveedor
        exclude = ['password1', 'password2', ]
        fields = ['username', 'email', 'first_name',
                  'last_name', 'identificacion', 'direccion', 'telefono', 'nacimiento', 'imagen','articulos']
    # end class

    def save(self, commit=True):
        operario = super(ProveedorFormEdit, self).save(commit)
        operario.is_staff = True
        operario.is_superuser = True
        operario.save()
        return operario
    # end def
# end class
