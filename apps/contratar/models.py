from django.db import models

# Create your models here.
#from __future__ import unicode_literals
from django.core.validators import EmailValidator


# Create your models here.
class contrata(models.Model):
	nombre= models.CharField(max_length=100)
	telefono=models.CharField(max_length=100)
	direccion=models.CharField(max_length=100)
	ciudad = models.TextField(max_length=100)
	fecha = models.TextField(max_length=100)


	def __unicode__(self):
		return self.nombre


