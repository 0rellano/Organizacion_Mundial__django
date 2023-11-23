# Vistas
from typing import Any
from urllib.parse import urlencode
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, TemplateView, DeleteView
from django.views.generic.edit import CreateView, UpdateView
from django.views import View
# Recursos
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse, reverse_lazy
from django.db.models import Q
# Aplicacion
from .forms import CustomUserCreationForm, JugadorForm, MundialForm, FaseForm
from .models import *


class homeView(TemplateView):
    template_name = 'index.html'


class Registro(View):
    template_name = 'registration/registro.html'
    form_class = CustomUserCreationForm

    def get(self, request, *args, **kwargs):
        data = {'form': self.form_class()}
        return render(request, self.template_name, data)

    def post(self, request, *args, **kwargs):
        formulario = self.form_class(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            return redirect(to="index")
        data = {'form': formulario}
        return render(request, self.template_name, data)

# JUGADORES

class ListaJugadoresView(ListView):
    model = Jugador
    template_name = 'jugador/lista_jugadores.html'
    context_object_name = 'jugadores'

    def get_queryset(self):
        queryset = Jugador.objects.all()
        buscar = self.request.GET.get('buscar')

        # Filtrar los jugadores según el parámetro de búsqueda  
        if buscar:
            # Modificar la búsqueda para que incluya jugadores que comienzan con la letra proporcionada
            queryset = queryset.filter(Q(nombre__istartswith=buscar) | Q(apellido__istartswith=buscar))

        # Obtener el parámetro 'ordenar_por' de la URL
        ordenar_por = self.request.GET.get('ordenar_por')

        # Aplicar la ordenación si el parámetro está presente
        if ordenar_por:
            queryset = queryset.order_by(ordenar_por)

        return queryset


class DetalleJugadorView(DetailView):
    model = Jugador
    template_name = 'jugador/detalle_jugador.html'
    context_object_name = 'jugador'
    pk_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['eventos'] = Evento.objects.filter(jugador=self.object).all()
        
        return context
    

class CrearJugadorView(CreateView):
    model = Jugador
    template_name = 'jugador/form_jugador.html'
    form_class = JugadorForm
    success_url = reverse_lazy('lista_jugadores')
        

class EditarJugadorView(UpdateView):
    model = Jugador
    template_name = 'jugador/form_jugador_update.html'
    form_class = JugadorForm
    success_url = reverse_lazy('lista_jugadores')


class ElimnarJugadorView(DeleteView):
    model = Jugador
    success_url = reverse_lazy('lista_jugadores')


# PAISES

class ListaPaisesView(ListView):
    model = Pais
    context_object_name = 'paises'
    template_name = 'pais/paises.html'
    

class PaisView(DetailView):
    model = Pais
    context_object_name = 'pais'
    template_name = 'pais/pais.html'
    pk_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        pais = self.object

        plantel_tecnico = pais.conocerPersonal()
        context['plantel_tecnico'] = plantel_tecnico

        equipos = Equipo.objects.filter(pais_perteneciente=pais)
        context['equipos'] = equipos

        ultimo_partido = Partido.objects.filter(Q(local=pais)|Q(visitante=pais)).order_by('fecha').last()
        context['formacion_actual'] = ultimo_partido.formacion_local if ultimo_partido.local == pais else ultimo_partido.formacion_visitante

        return context


# MUNDIALES

class ListaMundialesView(ListView):
    model = Mundial
    context_object_name = 'mundiales'
    template_name = 'mundial/mundiales.html'


class DetalleMundialView(DetailView):
    model = Mundial
    context_object_name = 'mundial'
    template_name = 'mundial/mundial.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Cambia 'pais' a 'self.object' ya que estás trabajando con un Mundial, no un País
        mundial = self.object
        fases = Fase.objects.filter(mundial=mundial).order_by('orden')
        partidos_por_fase = dict()
        for fase in fases:
            partidos = Partido.objects.filter(fase=fase)
            partidos_por_fase[fase] = partidos
        
        context['fases'] = partidos_por_fase
        context['participantes'] = Participante.objects.filter(mundial=mundial).order_by('posicion_obtenida')

        return context
    

class EliminarMundialView(DeleteView):
    model = Mundial
    success_url = reverse_lazy('mundiales')


class EditarMundialView(UpdateView):
    model = Mundial
    template_name = 'mundial/form_mundial_update.html'
    form_class = MundialForm
    
    def get_success_url(self) -> str:
        return reverse_lazy('fases_mundiales', kwargs={'pk': self.object.pk})


class CrearMundialView(CreateView):
    model = Mundial
    template_name = 'mundial/form_mundial.html'
    form_class = MundialForm

    def get_success_url(self) -> str:
        return reverse_lazy('fases_mundiales', kwargs={'pk': self.object.pk})
    

class ListaFasesMundialView(DetailView):
    model = Mundial
    template_name = 'mundial/fases_mundial.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['fases'] = Fase.objects.filter(mundial=self.object)
        return context


# FASES

class CrearFaseView(CreateView):
    model = Fase
    template_name = 'mundial/fase_form.html'
    form_class = FaseForm
    success_url = reverse_lazy('fases_mundiales')

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['pk_mundial'] = self.kwargs.get('mundial_id')
        return 

    def get_initial(self) -> dict[str, Any]:
        if self.request.method == 'GET':
            initial = super().get_initial()
            initial['mundial'] = Mundial.objects.get(pk=self.request.GET.get('pk')).pk
            initial['orden'] = self.request.GET.get('orden')
            return initial
    
    def get_success_url(self) -> str:
        return reverse_lazy('fases_mundiales', kwargs={'pk': int(self.request.GET.get('pk'))})
    

class EliminarFaseView(DeleteView):
    model = Fase

    def get(self, request, *args, **kwargs):
        self.request.session['previous_url'] = self.request.META.get('HTTP_REFERER', None)
        return super().get(request, *args, **kwargs)
    
    def get_success_url(self):
        previous_url = self.request.session.get('previous_url', None)
        return previous_url or super().get_success_url()





# PARTIDO

class PartidoView(DetailView):
    model = Partido
    context_object_name = 'partido'
    template_name = 'mundial/partido.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['eventos'] = Evento.objects.filter(partido=self.object).order_by('minuto_ocurrido')

        return context


