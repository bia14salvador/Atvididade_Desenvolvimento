from django.db import models

class Casa(models.Model):
    nome = models.CharField(max_length=100)
    responsavel = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    casa = models.ForeignKey(Casa, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
