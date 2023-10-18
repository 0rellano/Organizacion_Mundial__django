from django.urls import path
from django.urls import path
from .views import *

urlpatterns = [
    path('', homeView.as_view(), name='index'),
    path('jugadores/', ListaJugadoresView.as_view(), name='lista_jugadores'),
    path('jugadores/<int:pk>/', DetalleJugadorView.as_view(), name='detalle_jugador'),
    path('paises/', ListaPaisesView.as_view()),
    path('pais/<int:pk>', PaisView.as_view()),
    path('mundiales/', ListaMundialesView.as_view())
]