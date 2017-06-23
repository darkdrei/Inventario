# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.views import logout

# Create your views here.
class Logout(TemplateView):
    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return redirect('/admin/login/')
    # end def
# end class


class Home(TemplateView):
    def dispatch(self, request, *args, **kwargs):
        return redirect('/admin/')
    # end def
# end class
