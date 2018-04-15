# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-11-10 19:33
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='registrar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.IntegerField()),
                ('nombre', models.CharField(max_length=120)),
                ('apellido', models.CharField(max_length=120)),
                ('genero', models.CharField(max_length=120)),
                ('fechadenacimiento', models.DateField()),
                ('departamento', models.CharField(blank=True, max_length=500)),
                ('ciudad', models.CharField(blank=True, max_length=500)),
                ('email', models.EmailField(default='description email', max_length=254, validators=[django.core.validators.EmailValidator(message='Ingresa un email valido')])),
                ('direccion', models.CharField(default='description address text', max_length=120)),
            ],
        ),
    ]
