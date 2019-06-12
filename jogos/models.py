from django.db import models

class Jogos(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length = 45)

    def __str__(self):
        return self.nome
