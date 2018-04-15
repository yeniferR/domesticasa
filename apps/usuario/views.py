from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from apps.usuario.forms import RegistroForm
from django.shortcuts import render, redirect

# Create your views here.

class RegistroUsuario(CreateView):	
	model=User
	template_name="usuario/registro.html"
	form_class=RegistroForm
	
	success_url=reverse_lazy('home:home')