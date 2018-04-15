from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def preguntas(request):
	return render(request,'preguntas/preguntas.html')