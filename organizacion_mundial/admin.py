from django.contrib import admin
from .models import Pais, Jugador, Equipo, Personal, Rol

admin.site.register(Pais)
admin.site.register(Jugador)
admin.site.register(Equipo)
admin.site.register(Personal)
admin.site.register(Rol)