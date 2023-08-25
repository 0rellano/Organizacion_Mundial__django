from django.db import models

# Create your models here.

class Formacion(models.Model):
    delanteros = models.IntegerField()
    defensas = models.IntegerField()
    mediocampistas = models.IntegerField()


class Pais(models.Model):
    nombre = models.CharField(max_length=50)
    continente = models.CharField(max_length=20)
    abreviatura = models.CharField(max_length=5)
    formacion = models.OneToOneField(Formacion, on_delete=models.CASCADE)


class Jugadores(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    numero_camiseta = models.IntegerField()
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)