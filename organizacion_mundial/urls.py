from django.urls import path
from .views import *
from django.conf.urls import handler404

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
    path('paises/crear', CrearPaisView.as_view(), name='crear_pais'),
    #Mundial
    path('mundiales/', ListaMundialesView.as_view(), name='mundiales'),
    path('mundiales/<int:pk>', DetalleMundialView.as_view(), name='mundial'),
    path('partidos/<int:pk>', PartidoView.as_view(), name='partido'),
    #Registro
    path('registro/', Registro.as_view(), name='registro'),
    #Posiciones
    path('posiciones/crear', CrearPosicionView.as_view(), name='crear_posicion'),
    #Plantel
    path('plantel/crear', CrearPlantelView.as_view(), name='crear_plantel'),
]

handler404 = Error404View.as_view()
