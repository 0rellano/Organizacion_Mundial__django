from typing import Any
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.views import View
from .models import Jugador, Pais, Equipo, Mundial

class homeView(TemplateView):
    template_name = 'index.html'


class ListaJugadoresView(ListView):
    model = Jugador
    template_name = 'lista_jugadores.html'
    context_object_name = 'jugadores'

    def get_queryset(self):
        queryset = Jugador.objects.all()
        buscar = self.request.GET.get('buscar')

        # Filtrar los jugadores según el parámetro de búsqueda
        if buscar:
            # Modificar la búsqueda para que incluya jugadores que comienzan con la letra proporcionada
            queryset = queryset.filter(nombre__istartswith=buscar)

        # Obtener el parámetro 'ordenar_por' de la URL
        ordenar_por = self.request.GET.get('ordenar_por')

        # Aplicar la ordenación si el parámetro está presente
        if ordenar_por:
            queryset = queryset.order_by(ordenar_por)

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        pais = self.object

        plantel_tecnico = pais.conocerPersonal()
        context['plantel_tecnico'] = plantel_tecnico

        equipos = Equipo.objects.filter(pais_perteneciente=pais)
        context['equipos'] = equipos

        return context
    

class ListaMundialesView(ListView):
    model = Mundial
    context_object_name = 'mundiales'
    template_name = 'mundiales.html'
