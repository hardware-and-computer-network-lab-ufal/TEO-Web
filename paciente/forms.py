from django.forms import ModelForm

from paciente.models import Paciente

class Novo_Paciente_Form(ModelForm):
    class Meta:
        model = Paciente
        fields = [
            'cpf',
            'nome',
            'historico',
        ]

class Atualizar_Paciente_Form(ModelForm):
    class Meta:
        model = Paciente
        fields = [
            'nome',
            'historico',
        ]
