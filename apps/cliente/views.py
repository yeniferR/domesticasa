from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def cliente(request):
	return render(request,'cliente/cliente.html')

