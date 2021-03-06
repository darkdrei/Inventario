# -*- coding: utf-8 -*-
from django.contrib.auth.forms import UserCreationForm
from django import forms
from exileui.widgets import DatePickerWidget
import models
from django.contrib.admin import widgets


class UnidadNegocioForm(forms.ModelForm):
    class Meta:
        model = models.UnidadNegocio
        fields = ['nombre','descripcion']
        exclude = ['estado']
        widgets = {
            'descripcion': forms.Textarea,
        }
    #end class
#end class


class CajeroForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CajeroForm, self).__init__(*args, **kwargs)
        self.autenticate = ''
        self.fields['password1'].label = "Contraseña"
        self.fields['password2'].label = "Confirmar contraseña"
        self.fields['email'].label = "Correo Electrtónico"
        self.fields['first_name'].label = "Nombre"
        self.fields['last_name'].label = "Apellidos"
        self.fields['nacimiento'].widget = DatePickerWidget(
            attrs={'class': 'dateopera'},
            format="%d/%m/%Y")
        self.fields['telefono'].widget = forms.NumberInput()
    # end def

    def clean(self):
        data = super(CajeroForm, self).clean()
        if data.get('password1'):
            self.autenticate = data.get('password1')
        #end if
    #end def

    class Meta:
        model = models.Cajero
        fields = ['username', 'password1', 'password2', 'email', 'first_name',
                  'last_name', 'identificacion','departamento', 'negocio', 'direccion', 'telefono', 'nacimiento', 'imagen']
    # end class

    class Media:
        js = ('/static/empleados/js/dateoperario.js',)
    # end class

    def save(self, commit=True):
        recepcionista = super(CajeroForm, self).save(commit)
        recepcionista.is_staff = True
        recepcionista.is_superuser = True
        recepcionista.autenticate = self.autenticate
        recepcionista.save()
        return recepcionista
    # end def
# end class


class CajeroFormEdit(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CajeroFormEdit, self).__init__(*args, **kwargs)
        self.autenticate = ''
        self.fields['email'].label = "Correo Electrtónico"
        self.fields['first_name'].label = "Nombre"
        self.fields['last_name'].label = "Apellidos"
        self.fields['nacimiento'].widget = DatePickerWidget(
            attrs={'class': 'dateopera'},
            format="%d/%m/%Y")
        self.fields['telefono'].widget = forms.NumberInput()
    # end def

    class Meta:
        model = models.Cajero
        exclude = ['password1', 'password2', ]
        fields = ['username', 'email', 'first_name',
                  'last_name', 'identificacion','departamento',  'negocio', 'direccion', 'telefono', 'nacimiento', 'imagen']
    # end class

    class Media:
        js = ('/static/empleados/js/dateoperario.js',)
    # end class

    def clean(self):
        data = super(CajeroForm, self).clean()
        if data.get('password1'):
            self.autenticate = data.get('password1')
        #end if
    #end def

    def save(self, commit=True):
        recepcionista = super(CajeroFormEdit, self).save(commit)
        recepcionista.is_staff = True
        recepcionista.is_superuser = True
        recepcionista.autenticate = self.autenticate
        recepcionista.save()
        return recepcionista
    # end def
# end class


class AdministradorForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(AdministradorForm, self).__init__(*args, **kwargs)
        self.fields['password1'].label = "Contraseña"
        self.fields['password2'].label = "Confirmar contraseña"
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
        model = models.Administrador
        fields = ['username', 'password1', 'password2', 'email', 'first_name',
                  'last_name', 'identificacion','departamento', 'direccion', 'telefono', 'nacimiento', 'imagen']
    # end class

    def save(self, commit=True):
        cajero = super(AdministradorForm, self).save(commit)
        cajero.is_staff = True
        cajero.is_superuser = True
        cajero.save()
        return cajero
    # end def
# end class


class AdministradorFormEdit(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AdministradorFormEdit, self).__init__(*args, **kwargs)
        self.fields['email'].label = "Correo Electrtónico"
        self.fields['first_name'].label = "Nombre"
        self.fields['last_name'].label = "Apellidos"
        self.fields['nacimiento'].widget = DatePickerWidget(
            attrs={'class': 'dateopera'},
            format="%d/%m/%Y")
        self.fields['telefono'].widget = forms.NumberInput()
    # end def

    class Meta:
        model = models.Administrador
        exclude = ['password1', 'password2', ]
        fields = ['username', 'email', 'first_name',
                  'last_name', 'identificacion','departamento', 'direccion', 'telefono', 'nacimiento', 'imagen']
    # end class

    class Media:
        js = ('/static/empleados/js/dateoperario.js',)
    # end class

    def save(self, commit=True):
        cajero = super(AdministradorFormEdit, self).save(commit)
        cajero.is_staff = True
        cajero.is_superuser = True
        cajero.save()
        return cajero
    # end def
# end class
