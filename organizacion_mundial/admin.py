from django.contrib import admin
from .models import Pais, Jugador, Equipo, Personal, Rol, Mundial

admin.site.register(Pais)
admin.site.register(Jugador)
admin.site.register(Equipo)
admin.site.register(Personal)
admin.site.register(Rol)
admin.site.register(Mundial)