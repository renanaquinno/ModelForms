from django.db import models

# Create your models here.

class Carro(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class Cor(models.Model):
    cor = models.CharField(max_length=20)
    carro = models.ForeignKey(Carro, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline

class Time(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class Jogador(models.Model):
    jogador = models.CharField(max_length=20)
    time = models.ForeignKey(Time, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline


GENERO = (
    ('DR', 'Dr.'),
    ('DRA', 'Dra.'),
)

class Medico(models.Model):
    nome = models.CharField(max_length=20)
    genero = models.CharField(max_length=3, choices=GENERO)

    def __str__(self):
        return self.nome

class Hospital(models.Model):
    nome = models.CharField(max_length=20)
    Medico = models.ManyToManyField(Medico)

    def __str__(self):
        return self.nome


class Livro(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class Editora(models.Model):
    nome = models.CharField(max_length=20)
    livro = models.ManyToManyField(Livro)

    def __str__(self):
        return self.nome