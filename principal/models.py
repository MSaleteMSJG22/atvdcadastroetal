from django.db import models
from random import choices
from unittest.util import _MAX_LENGTH
from django.db import models

LISTA_SEXO = [
    ('Masculino', 'Masculino'),
    ('Feminino', 'Feminino')
]

LISTA_CURSO = [
    ('Curso Técnico', 'Curso Técnico')
]

class Aluno(models.Model):
    nome = models.CharField(max_length = 150)
    cpf = models.CharField(max_length = 15)
    data_nascimento = models.DateTimeField
    email = models.EmailField()
    endereço = models.CharField(max_length = 150)
    sexo = models.CharField(max_length = 150, choices = LISTA_SEXO)
    curso = models.CharField(max_length = 150, choices = LISTA_CURSO)

    def __str__(self):
        return self.nome