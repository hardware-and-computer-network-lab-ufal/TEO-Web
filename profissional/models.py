from django.db import models
from clinica.models import Clinica

class Profissional(models.Model):
	cpf = models.CharField(max_length = 45, primary_key = True)
	nome = models.CharField(max_length = 45)
	contato = models.CharField(max_length = 45)
	especialidade = models.CharField(max_length = 45)
	cnpj_clinica = models.ForeignKey(Clinica, on_delete=models.CASCADE)

	def __str__(self):
		return self.nome

class Trabalha_Em(models.Model):
	funcao = models.CharField(max_length = 45)
	cnpj_clinica = models.ForeignKey(Clinica, on_delete=models.CASCADE)
	cpf_profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE)
