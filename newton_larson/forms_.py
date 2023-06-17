from django import forms

class form_signup(forms.Form):
    username = forms.CharField(label='Nombre de Usuario', min_length=8,max_length=200, required=True)
    email = forms.CharField(label='Correo electrónico', max_length=200, required= True)
    password = forms.CharField(widget=forms.PasswordInput, label='Contraseña', min_length=8, required= True)
class form_login(forms.Form):
    username = forms.CharField(label='Nombre de Usuario', min_length=8,max_length=200, required=True)
    password = forms.CharField(widget=forms.PasswordInput, label='Contraseña', min_length=8, required= True)
    