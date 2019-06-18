# from django.contrib.auth.models import User
# from paciente.models import Paciente
from paciente.models import Paciente, PacienteJoga
from jogos.models import Jogos
from rest_framework import serializers

class JogosSerializer(serializers.ModelSerializer):
	class Meta:
		model = Jogos
		fields = ('id', 'nome')

class PacienteSerializer(serializers.ModelSerializer):
	class Meta:
		model = Paciente
		fields = ('cpf', 'nome')

class PacienteJogaSerializer(serializers.ModelSerializer):
	class Meta:
		model = PacienteJoga
		fields = ('id', 'tempoDeJogo', 'cpf', 'nome')

