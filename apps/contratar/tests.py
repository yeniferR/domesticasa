# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from contratar.forms import contratatatForm
from django.test import TestCase
from contratar.models import contrata


# Create your tests here.
class Testcontacto(TestCase):
    def test_contact_str(self):
        mycontact = contrata(nombre='Chérer')
        self.assertEqual(str(mycontact), 'Chérer'.encode('utf8'))

    def test_contact_str1(self):
        mycontact = contrata(nombre='fa21ere')
        self.assertEqual(str(mycontact), 'Chaarri'.encode('utf8'))

    def test_contact_str2(self):
        mycontact = contrata(nombre='fa21ere')
        self.assertEqual(str(mycontact), trabaj.nombre)

    def test_contact_str3(self):
    	trabaj.objects.create(nombre="haloe")
        mycontact = contrata(nombre='haloe')        
        self.assertEqual(str(mycontact), "haloe") 

    def test_unique_together_validation_should_work_for_person(self):
        data = contratatatForm({'email':'Norris@gmail.com'})
        self.assertFalse(data.is_valid())

    def test_email_used_by_django_auth_is_invalid(self):
        form = contratatatForm({'email': 'les@example.org'})
        self.assertFalse(form.is_valid())

    def test_email_used_by_django_auth_is_invalid1(self):
        form = contratatatForm({'email': 'lesre@xample.org'})
        self.assertFalse(form.is_valid())    
                   
