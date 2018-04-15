from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def limpieza(request):
	return render(request,'limpieza/limpieza.html')

