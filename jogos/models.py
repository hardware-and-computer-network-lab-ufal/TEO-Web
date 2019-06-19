from django.db import models

class Jogos(models.Model):
	nome = models.CharField(max_length = 45, primary_key=True)

	def __str__(self):
		return self.nome

