from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def servicios(request):
	return render(request,'sevicios/servicios.html')



