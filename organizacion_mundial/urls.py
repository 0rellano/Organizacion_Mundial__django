from django.urls import path
from django.urls import path
from .views import *

urlpatterns = [
    path('', homeView.as_view(), name='index'),
    path('jugadores/', ListaJugadoresView.as_view(), name='lista_jugadores'),
    path('jugadores/<int:pk>/', DetalleJugadorView.as_view(), name='detalle_jugador'),
    path('paises/', ListaPaisesView.as_view(), name='paises'),
    path('pais/<int:pk>', PaisView.as_view()),
    path('mundiales/', ListaMundialesView.as_view(), name='mundiales'),
<<<<<<< HEAD
=======
    path('mundiales/<int:pk>', DetalleMundialView.as_view())
>>>>>>> 77fabf3 (Correcion de errores de commits)
]