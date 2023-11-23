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
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Aplicacion
from .forms import *
from .models import *
from django.urls import reverse
from datetime import date
from django.db.models import F


class homeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mundial_actual'] = Mundial.objects.filter(fecha_final__lte=date.today()).order_by('-fecha_final').first()
        return context

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
@method_decorator(login_required(login_url='login'), name='dispatch')
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
            if ordenar_por.startswith('-'):
                # Orden descendente
                campo_orden = ordenar_por[1:]
                queryset = queryset.order_by(F(campo_orden).desc())
            else:
                # Orden ascendente
                queryset = queryset.order_by(ordenar_por)

        print("Ordenar por:", ordenar_por)
        print(queryset.query)  # Imprimir la consulta SQL generada
        return queryset


@method_decorator(login_required(login_url='login'), name='dispatch')
class DetalleJugadorView(DetailView):
    model = Jugador
    template_name = 'jugador/detalle_jugador.html'
    context_object_name = 'jugador'
    pk_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['eventos'] = Evento.objects.filter(jugador=self.object).all()
        
        return context


@method_decorator(login_required(login_url='login'), name='dispatch')
class CrearJugadorView(CreateView):
    model = Jugador
    template_name = 'jugador/form_jugador.html'
    form_class = JugadorForm
    success_url = reverse_lazy('lista_jugadores')


@method_decorator(login_required(login_url='login'), name='dispatch')
class EditarJugadorView(UpdateView):
    model = Jugador
    template_name = 'jugador/form_jugador_update.html'
    form_class = JugadorForm
    success_url = reverse_lazy('lista_jugadores')


@method_decorator(login_required(login_url='login'), name='dispatch')
class ElimnarJugadorView(DeleteView):
    model = Jugador
    success_url = reverse_lazy('lista_jugadores')


# PAISES
@method_decorator(login_required(login_url='login'), name='dispatch')
class CrearPaisView(CreateView):
    model = Pais
    template_name = 'pais/form_pais.html'
    form_class = PaisForm
    success_url = reverse_lazy('paises')


@method_decorator(login_required(login_url='login'), name='dispatch')
class EliminarPaisView(DeleteView):
    model = Pais
    success_url = reverse_lazy('paises')
    

@method_decorator(login_required(login_url='login'), name='dispatch')
class EditarPaisView(UpdateView):
    model = Pais
    template_name = 'pais/form_pais_update.html'
    form_class = PaisForm
    success_url = reverse_lazy('paises')


@method_decorator(login_required(login_url='login'), name='dispatch')
class CrearPlantelView(CreateView):
    model = Persona
    template_name = 'plantel/form_plantel.html'
    form_class = PlantelForm
    success_url = reverse_lazy('paises')


@method_decorator(login_required(login_url='login'), name='dispatch')
class CrearEquipoView(CreateView):
    model = Equipo
    template_name = 'pais/form_equipo.html'
    form_class = EquipoForm
    def get_success_url(self):
        if self.object and self.object.pais_perteneciente:
            pais_id = self.object.pais_perteneciente.id
            return reverse('pais', args=[pais_id])
        else:
            return reverse('')

class EditarEquipoView(UpdateView):
    model = Equipo
    template_name = 'pais/form_equipo_update.html'
    form_class = EquipoForm
    def get_success_url(self):
            pais_id = self.object.pais_perteneciente.id
            return reverse('pais', args=[pais_id])

@method_decorator(login_required(login_url='login'), name='dispatch')
class EliminarEquipoView(DeleteView):
    model = Equipo
    def get_success_url(self):
            pais_id = self.object.pais_perteneciente.id
            return reverse('pais', args=[pais_id])

# Vistas para formaciones
@method_decorator(login_required(login_url='login'), name='dispatch')
class CrearFormacionView(CreateView):
    model = Formacion
    template_name = 'pais/form_formacion.html'
    form_class = FormacionForm
    def get_success_url(self):
        if self.object and self.object.pais_perteneciente:
            pais_id = self.object.pais_perteneciente.id
            return reverse('pais', args=[pais_id])
        else:
            return reverse('')

@method_decorator(login_required(login_url='login'), name='dispatch')
class EditarFormacionView(UpdateView):
    model = Formacion
    template_name = 'pais/form_formacion_update.html'
    form_class = FormacionForm
    def get_success_url(self):
        pais_id = self.object.pais_perteneciente.id
        return reverse('pais', args=[pais_id])

@method_decorator(login_required(login_url='login'), name='dispatch')
class EliminarFormacionView(DeleteView):
    model = Formacion
    def get_success_url(self):
        pais_id = self.object.pais_perteneciente.id
        return reverse('pais', args=[pais_id])

# Vistas para empleados (plantel técnico)
@method_decorator(login_required(login_url='login'), name='dispatch')
class CrearEmpleadoView(CreateView):
    model = Personal
    template_name = 'pais/form_plantel.html'
    form_class = EmpleadoForm
    def get_success_url(self):
        if self.object and self.object.pais_perteneciente:
            pais_id = self.object.pais_perteneciente.id
            return reverse('pais', args=[pais_id])
        else:
            return reverse('')

@method_decorator(login_required(login_url='login'), name='dispatch')
class EditarEmpleadoView(UpdateView):
    model = Personal
    template_name = 'pais/form_plantel_update.html'
    form_class = EmpleadoForm
    def get_success_url(self):
        pais_id = self.object.pais_perteneciente.id
        return reverse('pais', args=[pais_id])

@method_decorator(login_required(login_url='login'), name='dispatch')
class EliminarEmpleadoView(DeleteView):
    model = Personal
    def get_success_url(self):
        pais_id = self.object.pais_perteneciente.id
        return reverse('pais', args=[pais_id])

@method_decorator(login_required(login_url='login'), name='dispatch')


class ListaPaisesView(ListView):
    model = Pais
    context_object_name = 'paises'
    template_name = 'pais/paises.html'

    def get_queryset(self):
        queryset = Pais.objects.all()
        buscar = self.request.GET.get('buscar')

        # Filtrar los países según el parámetro de búsqueda
        if buscar:
            queryset = queryset.filter(nombre__istartswith=buscar)

        # Obtener el parámetro 'ordenar_por' de la URL
        ordenar_por = self.request.GET.get('ordenar_por')

        # Aplicar la ordenación si el parámetro está presente
        if ordenar_por:
            if ordenar_por.startswith('-'):
                # Orden descendente
                campo_orden = ordenar_por[1:]
                queryset = queryset.order_by(F(campo_orden).desc())
            else:
                # Orden ascendente
                queryset = queryset.order_by(F(ordenar_por))

        return queryset
    

@method_decorator(login_required(login_url='login'), name='dispatch')
class PaisView(DetailView):
    model = Pais
    context_object_name = 'pais'
    template_name = 'pais/pais.html'
    pk_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        pais = self.object

        # Obtiene el plantel técnico
        plantel_tecnico = pais.conocerPersonal()

        # Calcula la edad para cada empleado
        for empleado in plantel_tecnico:
            if empleado.fecha_nacimiento:
                hoy = date.today()
                edad = hoy.year - empleado.fecha_nacimiento.year - ((hoy.month, hoy.day) < (empleado.fecha_nacimiento.month, empleado.fecha_nacimiento.day))
                empleado.edad = edad
            else:
                empleado.edad = None

        context['plantel_tecnico'] = plantel_tecnico

        equipos = Equipo.objects.filter(pais_perteneciente=pais)
        context['equipos'] = equipos

        ultimo_partido = Partido.objects.filter(Q(local=pais) | Q(visitante=pais)).order_by('fecha').last()

        if ultimo_partido:
            context['formacion_actual'] = ultimo_partido.formacion_local if ultimo_partido.local == pais else ultimo_partido.formacion_visitante
        else:
            context['formacion_actual'] = None

        return context


# MUNDIALES

@method_decorator(login_required(login_url='login'), name='dispatch')
class ListaMundialesView(ListView):
    model = Mundial
    context_object_name = 'mundiales'
    template_name = 'mundial/mundiales.html'


@method_decorator(login_required(login_url='login'), name='dispatch')
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
        return reverse_lazy('fases_mundial', kwargs={'pk': self.object.pk})
    

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
    success_url = reverse_lazy('fases_mundial')

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['pk_mundial'] = self.kwargs.get('mundial_id')
        return  context

    def get_initial(self) -> dict[str, Any]:
        if self.request.method == 'GET':
            self.request.session['id_mundial'] = self.request.GET.get('pk')
            initial = super().get_initial()
            initial['mundial'] = Mundial.objects.get(pk=self.request.GET.get('pk')).pk
            initial['orden'] = self.request.GET.get('orden')
            return initial
    
    def get_success_url(self) -> str:
        return reverse_lazy('fases_mundial', kwargs={'pk': self.request.session.get('id_mundial')})
    

class EliminarFaseView(DeleteView):
    model = Fase

    def get_success_url(self) -> str:
        pk_mundial = self.object.mundial.pk
        return reverse_lazy('fases_mundial', kwargs={'pk': pk_mundial})


class EditarFaseView(UpdateView):
    model = Fase
    template_name = 'mundial/fase_form_update.html'
    form_class = FaseForm
    success_url = reverse_lazy('fases_mundial')

    def get_success_url(self) -> str:
        pk_mundial = self.object.mundial.pk
        return reverse_lazy('fases_mundial', kwargs={'pk': pk_mundial})

# PARTIDO
@method_decorator(login_required(login_url='login'), name='dispatch')
class PartidoView(DetailView):
    model = Partido
    context_object_name = 'partido'
    template_name = 'mundial/partido.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['eventos'] = Evento.objects.filter(partido=self.object).order_by('minuto_ocurrido')

        return context


class Error404View(View):
    def get(self, request, exception=None, *args, **kwargs):
        return render(request, '404.html', status=404)