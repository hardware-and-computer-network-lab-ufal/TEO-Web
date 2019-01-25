from django.db import models

class Paciente(models.Model):
	cpf = models.CharField(max_length = 45, primary_key = True)
	nome = models.CharField(max_length = 45)
	historico = models.CharField(max_length = 45)

	def __str__(self):
		return self.nome
