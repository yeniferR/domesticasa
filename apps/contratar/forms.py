from django import forms


class contratatatForm(forms.Form):
	nombre= forms.CharField(required =False, max_length=100,  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su nombre'}))
	telefono=forms.CharField(required =False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su telefono'}))
	direccion=forms.CharField(required =False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su direccion'}))
	ciudad = forms.CharField(required=True,max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la ciudad donde vive'}))
	fecha = forms.CharField(required=True,max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la fecha'}))
