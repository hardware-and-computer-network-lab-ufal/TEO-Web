# from django.contrib.auth.models import User
from paciente.models import Paciente
from rest_framework import serializers

# class UserSerializer(serializers.HyperlinkedModelSerializer):
# 	class Meta:
# 		model = User
# 		fields = ('url', 'username', 'email')

class PacienteSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Paciente
		fields = ('cpf', 'nome')