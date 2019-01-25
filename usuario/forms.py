from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

Usuario = get_user_model()

class Cadastro_Form(UserCreationForm):

    class Meta:
        model = Usuario
        fields = ['username', 'email']

class Editar_Perfil_Form(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = ['username', 'email']
