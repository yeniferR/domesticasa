from django import forms


class trabajtForm(forms.Form):
	nombre= forms.CharField(required =False, max_length=100,  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su nombre'}))
	apellido=forms.CharField(required =False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su apeliido'}))
	telefono=forms.CharField(required =False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su telefono'}))
	cedula=forms.CharField(required =False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su cedula'}))
	email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su correo'}))
	ciudad = forms.CharField(required=True,max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la ciudad donde vive'}))
