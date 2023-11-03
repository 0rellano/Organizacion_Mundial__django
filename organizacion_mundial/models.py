from django.db import models
from django.core.exceptions import ValidationError
from datetime import date
from django.core.validators import MinValueValidator
from django.db.models import Q


class Mundial(models.Model):
    anio = models.CharField(max_length=100)
    pais_sede = models.ForeignKey("Pais", on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_final = models.DateField()

    def __str__(self) -> str:
        return f'Mundial {self.pais_sede.nombre} {self.anio}'


class Fase(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=300)
    fecha_inicio = models.DateField()
    fecha_final = models.DateField()
    orden = models.PositiveSmallIntegerField()
    mundial = models.ForeignKey('Mundial', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"FASE {self.mundial} {self.nombre}"


class Formacion(models.Model):
    FORMACION_CHOICES = [
        ('4-4-2', '4-4-2'),
        ('4-3-3', '4-3-3'),
        ('3-5-2', '3-5-2'),
        ('4-2-4', '4-2-4'),
        ('4-2-3-1', '4-2-3-1'),
        ('4-3-2-1', '4-3-2-1'),
        ('3-4-3', '3-4-3'),
    ]
    pais = models.ForeignKey('Pais', on_delete=models.CASCADE)
    esquema = models.CharField(max_length=10, choices=FORMACION_CHOICES, default='4-4-2')
    titulares = models.ManyToManyField('Jugador', related_name='jugadores_titulares')
    suplentes = models.ManyToManyField('Jugador', related_name='jugadores_suplentes')

    def __str__(self) -> str:
        return f'{self.pk}:{self.esquema} {self.pais}'


class Partido(models.Model):
    fecha = models.DateField()
    local = models.ForeignKey('Pais', related_name='pais_local', on_delete=models.SET_NULL, null=True)
    visitante = models.ForeignKey('Pais', related_name='pais_visitante', on_delete=models.SET_NULL, null=True)
    goles_local = models.PositiveSmallIntegerField()
    goles_visitante = models.PositiveSmallIntegerField()
    minutos_ataque_local = models.PositiveSmallIntegerField()
    cantidad_corners_local = models.PositiveSmallIntegerField()
    cantidad_laterales_local = models.PositiveSmallIntegerField()
    minutos_ataque_visitante = models.PositiveSmallIntegerField()
    cantidad_corners_visitante = models.PositiveSmallIntegerField()
    cantidad_laterales_visitante = models.PositiveSmallIntegerField()
    formacion_local = models.ForeignKey('Formacion', on_delete=models.CASCADE, related_name='formacion_local', null=True)
    formacion_visitante = models.ForeignKey('Formacion', on_delete=models.CASCADE, related_name='formacion_visitante', null=True)
    fase = models.ForeignKey('Fase', on_delete=models.CASCADE)

    def gano_local(self):
        if self.goles_local > self.goles_visitante:
            return self.local
        elif self.goles_visitante > self.goles_local:
            return self.visitante
        return None

    def __str__(self) -> str:
        return f'{self.local} ({self.goles_local}) - {self.visitante} ({self.goles_visitante}): {self.fecha}'
    



class Evento(models.Model):
    minuto_ocurrido = models.PositiveSmallIntegerField()
    jugador = models.ForeignKey('Jugador', on_delete=models.SET_NULL, null=True)
    tipo_evento = models.ForeignKey('TipoEvento', on_delete=models.SET_NULL, null=True)
    partido = models.ForeignKey('Partido', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.tipo_evento} de {self.jugador} al {self.minuto_ocurrido}   PARTIDO: {self.partido} "


class TipoEvento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=300)

    def __str__(self) -> str:
        return self.nombre


class Participante(models.Model):
    pais = models.ForeignKey('Pais', on_delete=models.CASCADE)
    posicion_obtenida = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)])
    mundial = models.ForeignKey('Mundial', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.pais.nombre} - Posición {self.posicion_obtenida} - Mundial {self.mundial.anio}"

class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=300)
    pais_perteneciente = models.ForeignKey('Pais', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nombre
      

class Pais(models.Model):
    nombre = models.CharField(max_length=100)
    liga_nombre = models.CharField(max_length=150)

    def conocerPersonal(self):
        return Personal.objects.filter(pais_perteneciente=self)
    
    def conocerEstadistica(self) -> dict:
        estadistica = {
            'minutos_ataque': 0,
            'cantidad_corners': 0,
            'cantidad_laterales': 0
        }
        for partido in self.obtenerTodosPartidos():
            estadistica['minutos_ataque'] += partido.minutos_ataque
            estadistica['cantidad_corners'] += partido.cantidad_corners
            estadistica['cantidad_laterales'] += partido.cantidad_laterales
        return estadistica
    
    def mundiales_ganados(self):
        return Participante.objects.filter(pais=self, posicion_obtenida=1).count()
    
    def __str__(self):
        return self.nombre


class Persona(models.Model):
    class Meta:
        abstract = True

    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    nro_pasaporte = models.CharField(max_length=200)
    fecha_nacimiento = models.DateField(default=date(2005, 1, 1))

    def obtener_edad(self):
        fecha_actual = date.today()
        return self.fecha_nacimiento.year - fecha_actual.year
    
    def __str__(self) -> str:
        return f'{self.nombre} {self.apellido} {self.nro_pasaporte}'
    

class Jugador(Persona):
    numero_camiseta = models.IntegerField()
    pais = models.ForeignKey('Pais', on_delete=models.CASCADE)
    equipo = models.ForeignKey('Equipo', on_delete=models.SET_NULL, null=True)
    posicion = models.ForeignKey('Posicion', on_delete=models.SET_NULL, null=True)
    fecha_retiro = models.DateField(null=True, default=None, blank=True)
    def sigue_jugando(self):
        return self.fecha_retiro != None
    
    def clean(self):
        super().clean()

        if self.numero_camiseta is not None and self.numero_camiseta < 0:
            raise ValidationError('El número de camiseta no puede ser negativo.')
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"



class Rol(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=300)

    def __str__(self) -> str:
        return self.nombre


class Personal(Persona):
    fecha_comienzo = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    pais_perteneciente = models.ForeignKey('Pais', on_delete=models.SET_NULL, null=True)
    rol = models.ForeignKey('Rol', on_delete=models.SET_NULL, null=True)

    def sigue_trabajando(self):
        return self.fecha_fin == None

    def __str__(self) -> str:
        return f"{self.rol.__str__()}, {super().__str__()}"


class Posicion(models.Model):
    nombre_posicion = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=300)

    def __str__(self):
        return self.nombre_posicion