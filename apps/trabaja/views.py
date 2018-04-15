from django.shortcuts import render

from django.core.mail import send_mail
from django.conf import settings

from .forms import trabajtForm

def trabaja(request):
	title='¿Quieres trabajar con nosotros? envianos tus datos.'
	form = trabajtForm(request.POST or None)
	context = {'title': title, 'form':form, }
	

	if form.is_valid():
		name = form.cleaned_data['nombre']
		name1=form.cleaned_data['apellido']
		name2=form.cleaned_data['telefono']
		name3=form.cleaned_data['cedula']
		comment = form.cleaned_data['ciudad']
		print ( form.cleaned_data['email'])
		subject = 'Mensaje de Usuario'
		message = '%s %s %s %s %s' %(name,name1,name2,name3,comment)
		emailFrom = form.cleaned_data['email']
		emailTo = [settings.EMAIL_HOST_USER]
		send_mail(subject, message, emailFrom, emailTo, fail_silently=True)	
		title="Gracias !"
		confirm_message ="El mensaje ha sido enviado, una persona de nuestro equipo te llamará en menos de 48 horas"
		context = {'title': title, 'confirm_message':confirm_message, }

	template = 'trabaja/trabaja.html'
	return render(request,template,context)