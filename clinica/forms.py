from django import forms
from clinica.models import Clinica

class Nova_Clinica_Form(forms.ModelForm):
    class Meta:
        model = Clinica
        fields = [
            'cnpj',
            'nome',
            'endereco',
            'contato',
        ]

class Atualizar_Clinica_Form(forms.ModelForm):
    class Meta:
        model = Clinica
        fields = [
            'nome',
            'endereco',
            'contato',
        ]
