from django.db import models

class Clinica(models.Model):
	cnpj = models.CharField(max_length = 45, primary_key = True)
	nome = models.CharField(max_length = 45)
	endereco = models.CharField(max_length = 45)
	contato = models.CharField(max_length = 45)

	def __str__(self):
		return self.nome
