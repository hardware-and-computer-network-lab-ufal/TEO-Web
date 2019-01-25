from django.forms import ModelForm
from profissional.models import Profissional

class Novo_Profissional_Form(ModelForm):
    class Meta:
        model = Profissional
        fields = [
            'cpf',
            'nome',
            'contato',
            'especialidade',
            'cnpj_clinica',
        ]

class Atualizar_Profissional_Form(ModelForm):
    class Meta:
        model = Profissional
        fields = [
            'nome',
            'contato',
            'especialidade',
            'cnpj_clinica',
        ]
