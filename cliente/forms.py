# -*- coding: utf-8 -*-
from django.contrib.auth.forms import UserCreationForm
from django import forms
import models
from exileui.widgets import DatePickerWidget
from django.contrib.admin import widgets


class ClienteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ClienteForm, self).__init__(*args, **kwargs)
        self.fields['email'].label = "Correo Electrtónico"
        self.fields['first_name'].label = "Nombre"
        self.fields['last_name'].label = "Apellidos"
        self.fields['nacimiento'].widget = DatePickerWidget(
            attrs={'class': 'dateopera'},
            format="%d/%m/%Y")
        self.fields['telefono'].widget = forms.NumberInput()
    # end def

    class Meta:
        model = models.Ciente
        fields = ['first_name',
                  'last_name', 'identificacion', 'credito', 'direccion', 'telefono','email', 'nacimiento', 'imagen']
        exclude = ['username', 'password1', 'password2']
    # end class

    class Media:
        js = ('/static/empleados/js/dateoperario.js',)
    # end class

    def save(self, commit=True):
        recepcionista = super(ClienteForm, self).save(commit)
        recepcionista.is_staff = True
        recepcionista.is_superuser = True
        recepcionista.save()
        return recepcionista
    # end def
# end class


class ClienteFormEdit(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ClienteFormEdit, self).__init__(*args, **kwargs)
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
        model = models.Ciente
        exclude = ['username', 'password1', 'password2']
        fields = ['first_name',
                  'last_name', 'identificacion', 'direccion','credito', 'telefono','email', 'nacimiento', 'imagen']
    # end class

    class Media:
        js = ('/static/empleados/js/dateoperario.js',)
    # end class

    def save(self, commit=True):
        recepcionista = super(ClienteFormEdit, self).save(commit)
        recepcionista.is_staff = True
        recepcionista.is_superuser = True
        recepcionista.autenticate = self.autenticate
        recepcionista.save()
        return recepcionista
    # end def
# end class
