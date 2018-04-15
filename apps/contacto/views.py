from django.shortcuts import render

from django.core.mail import send_mail
from django.conf import settings

from .forms import contactForm

def contacto(request):
	title='Contacto'
	form = contactForm(request.POST or None)
	context = {'title': title, 'form':form, }
	

	if form.is_valid():
		name = form.cleaned_data['nombre']
		name1 = form.cleaned_data['email']
		comment = form.cleaned_data['mensaje']
		print ( form.cleaned_data['email'])
		subject = 'Mensaje'
		message = '%s %s %s ' %(name,comment,name1)
		emailFrom = form.cleaned_data['email']
		emailTo = [settings.EMAIL_HOST_USER]
		send_mail(subject, message, emailFrom, emailTo, fail_silently=True)	

	template = 'contacto/contacto.html'
	return render(request,template,context)
