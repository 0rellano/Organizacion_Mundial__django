import queue
from django.db import models

class Mundial(models.Model):
    nombre = models.CharField(max_length=100)
    pais_sede = models.ForeignKey("Pais", on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_final = models.DateField()


class Fase(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=300)
    fecha_inicio = models.DateField()
    fecha_final = models.DateField()
    mundial = models.ForeignKey('Mundial', on_delete=models.CASCADE)


class Partido(models.Model):
    fecha = models.DateField()
    local = models.ForeignKey('Pais', on_delete=models.SET_NULL)
    visitante = models.ForeignKey('Pais', on_delete=models.SET_NULL)
    goles_local = models.PositiveSmallIntegerField()
    goles_visitante = models.PositiveSmallIntegerField()
    minutos_ataque = models.PositiveSmallIntegerField()
    cantidad_corners = models.PositiveSmallIntegerField()
    cantidad_laterales = models.PositiveSmallIntegerField()
    fase = models.ForeignKey('Fase', on_delete=models.CASCADE)

    def gano_local(self):
        if self.goles_local > self.goles_visitante:
            return self.local
        elif self.goles_visitante > self.goles_local:
            return self.visitante
        return None
    

class Evento(models.Model):
    minuto_ocurrido = models.PositiveSmallIntegerField()
    jugador = models.ForeignKey("Jugador")
    tipo_evento = models.ForeignKey('TipoEvento')


class TipoEvento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=300)


class Participante(models.Model):
    pais = models.ForeignKey('Pais', on_delete=models.CASCADE)
    posicion_obtenida = models.PositiveSmallIntegerField()


class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=300)
    pais_perteneciente = models.ForeignKey('Pais', on_delete=models.SET_NULL)
      

class Formacion(models.Model):
    esquema = models.CharField(max_length=50)
    jugadores = models.ManyToManyField(Jugador)


class Pais(models.Model):
    nombre = models.CharField(max_length=100)
    liga_nombre = models.CharField(max_length=150)
    formacion = models.ForeignKey(Formacion, on_delete=models.CASCADE)

    def conocerPersonal(self):
        return Personal.objects.filter(pais_perteneciente=self)
    
    def obtenerTodosPartidos(self):
        return Partido.objects.filter(Q(local=self) | Q(visitante=self))
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
    
    def conocerFormacionActual(self):
        from django.utils import timezone
        fecha_actual = timezone.now()
        partido_mas_cercano = Partido.objects.filter(
        Q(local=self) | Q(visitante=self), fecha__gte=fecha_actual).order_by('fecha').first()



class Persona(models.Model):
    class Meta:
        abstract = True

    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    nro_pasaporte = models.CharField(max_length=200)
    fecha_nacimiento = models.DateField()

    def obtener_edad(self):
        from datetime import date

        fecha_actual = date.today()
        return self.fecha_nacimiento.year - fecha_actual.year

class Jugador(Persona):
    numero_camiseta = models.IntegerField()
    pais = models.ForeignKey('Pais', on_delete=models.CASCADE)
    equipo = models.ForeignKey('Equipo', on_delete=models.SET_NULL)
    posicion = models.ForeignKey('Posicion', on_delete=models.SET_NULL)
    fecha_retiro = models.DateField(null=True, default=None)

    def sigue_jugando(self):
        return self.fecha_retiro != None



class Rol(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=300)


class Personal(Persona):
    fecha_comienzo = models.DateField()
    fecha_fin = models.DateField()
    rol = models.ForeignKey(Rol, on_delete=models.SET_NULL)
    pais_perteneciente = models. ForeignKey(Pais, on_delete=models.SET_NULL)


class Posicion(models.Model):
    nombre_posicion = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=300)

