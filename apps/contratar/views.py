from django.shortcuts import render

# Create your views here.

from django.core.mail import send_mail
from django.conf import settings

from .forms import contratatatForm

def contratar(request):
	title='Contrar Usuario'
	form = contratatatForm(request.POST or None)
	context = {'title': title, 'form':form, }
	

	if form.is_valid():
		name = form.cleaned_data['nombre']
		name1=form.cleaned_data['telefono']
		name2=form.cleaned_data['direccion']
		name3=form.cleaned_data['fecha']
		comment = form.cleaned_data['ciudad']

		print ( form.cleaned_data['nombre'])
		subject = 'Contratacion de Usuario'
		message = '%s %s %s %s %s' %(name,name1,name2,name3,comment)
		emailFrom = form.cleaned_data['nombre']
		emailTo = [settings.EMAIL_HOST_USER]
		send_mail(subject, message, emailFrom, emailTo, fail_silently=True)	
		

	template = 'contratar/contratar.html'
	return render(request,template,context)
