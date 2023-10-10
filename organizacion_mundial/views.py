from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.views import View
from .models import Jugador, Pais

class homeView(TemplateView):
    template_name = 'index.html'

class ListaJugadoresView(ListView):
    model = Jugador
    template_name = 'lista_jugadores.html'
    context_object_name = 'jugadores'
    ordering = ['nombre']  # Orden predeterminado por nombre

    def get_queryset(self):
        queryset = Jugador.objects.all()
        ordering = self.request.GET.get('ordenar_por')

        if ordering == 'pais':
            queryset = queryset.order_by('pais__nombre', 'nombre')
        elif ordering == 'posicion':
            queryset = queryset.order_by('posicion', 'nombre')

        return queryset



class DetalleJugadorView(DetailView):
    model = Jugador
    template_name = 'detalle_jugador.html'
    context_object_name = 'jugador'
    pk_url_kwarg = 'pk'

class ListaPaisesView(ListView):
    model = Pais
    context_object_name = 'paises'
    template_name = 'paises.html'
    
class PaisView(DetailView):
    model = Pais
    context_object_name = 'pais'
    template_name = 'pais.html'
    pk_url_kwarg = 'pk'