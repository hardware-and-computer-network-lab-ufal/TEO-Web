from django.db import models
from jogos.models import Jogos

class Paciente(models.Model):
	cpf = models.CharField(max_length = 45, primary_key = True)
	nome = models.CharField(max_length = 45)
	historico = models.CharField(max_length = 45)

	def __str__(self):
		return self.nome

class PacienteJoga(models.Model):
	cpf = models.ForeignKey(Paciente, on_delete=models.CASCADE, default="Null")
	nomeJogo = models.ForeignKey(Jogos, on_delete=models.CASCADE)
	tempoJogo = models.PositiveIntegerField()
	quantidadeAcertos = models.PositiveIntegerField()
	quantidadeErros = models.PositiveIntegerField()
	horario = models.DateTimeField(auto_now_add=True)
