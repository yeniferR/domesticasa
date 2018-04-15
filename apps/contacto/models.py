# -*- coding: utf-8 -*-
from django.db import models
#from __future__ import unicode_literals
from django.core.validators import EmailValidator


# Create your models here.
class trabaj(models.Model):
	nombre= models.CharField(max_length=100)
	email = models.EmailField(blank=False, validators=[EmailValidator(message="Ingresa un email valido")], default='description email')
	mensaje = models.TextField(max_length=100)


	def __unicode__(self):
		return self.nombre