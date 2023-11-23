from django.urls import path
from .views import *

urlpatterns = [
    path('', homeView.as_view(), name='index'),
    #Jugador
    path('jugadores/', ListaJugadoresView.as_view(), name='lista_jugadores'),
    path('jugadores/<int:pk>/', DetalleJugadorView.as_view(), name='detalle_jugador'),
    path('jugadores/crear', CrearJugadorView.as_view(), name='crear_jugador'),
    path('jugadores/delete/<int:pk>', ElimnarJugadorView.as_view(), name='eliminar_jugador'),
    path('jugadores/editar/<int:pk>', EditarJugadorView.as_view(), name='editar_jugador'),
    #Pais
    path('paises/', ListaPaisesView.as_view(), name='paises'),
    path('pais/<int:pk>', PaisView.as_view(), name='pais'),
    #Mundial
    path('mundiales/', ListaMundialesView.as_view(), name='mundiales'),
    path('mundial/crear', CrearMundialView.as_view(), name='crear_mundial'),
    path('mundial/eliminar/<int:pk>', EliminarMundialView.as_view(), name='eliminar_mundial'),
    path('mundial/editar/<int:pk>', EditarMundialView.as_view(), name='editar_mundial'),
    path('mundial/<int:pk>', DetalleMundialView.as_view(), name='mundial'),
    # Fase
    path('mundial/fases/<int:pk>', ListaFasesMundialView.as_view(), name='fases_mundiales'),
    path('fase/crear/<int:pk>', CrearFaseView.as_view(), name='crear_fase'),
    path('fase/eliminar/<int:pk>', EliminarFaseView.as_view(), name='eliminar_fase'),
    #Partido
    path('partidos/<int:pk>', PartidoView.as_view(), name='partido'),
    #Registro
    path('registro/', Registro.as_view(), name='registro'),
]