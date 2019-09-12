from django.db import models


class Aluno (models.Model):
    nome = models.CharField(max_length=50)
    matricula = models.CharField(max_length=11)
    sexo = models.CharField(max_length=10)
    idade= models.CharField(max_length=50)

    def __str__(self):
        return self.nome

# Create your models here.
Aluno.objects.filter(matricula=1003)