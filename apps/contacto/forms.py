from django import forms


class contactForm(forms.Form):
	nombre= forms.CharField(required =False, max_length=100,  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su nombre'}))
	email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su correo'}))
	mensaje = forms.CharField(required=True,max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su mensaje'}))
