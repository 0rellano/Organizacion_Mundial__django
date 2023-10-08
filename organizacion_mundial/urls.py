from django.urls import path
from organizacion_mundial.views import index
from django.urls import path
from .views import ListaJugadoresView, DetalleJugadorView

urlpatterns = [
    path('', index, name='index'),
    path('jugadores/', ListaJugadoresView.as_view(), name='lista_jugadores'),
    path('jugadores/<int:pk>/', DetalleJugadorView.as_view(), name='detalle_jugador')
]