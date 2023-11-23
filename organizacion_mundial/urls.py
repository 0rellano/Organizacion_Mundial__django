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
    #Paises
    path('paises/', ListaPaisesView.as_view(), name='paises'),
    path('pais/<int:pk>', PaisView.as_view(), name='pais'),
    path('paises/crear', CrearPaisView.as_view(), name='crear_pais'),
    path('paises/delete/<int:pk>', EliminarPaisView.as_view(), name='eliminar_pais'),
    path('paises/editar/<int:pk>', EditarPaisView.as_view(), name='editar_pais'),
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
    #Plantel
    path('plantel/crear', CrearPlantelView.as_view(), name='crear_plantel'),
    # Equipos
    path('equipos/crear', CrearEquipoView.as_view(), name='crear_equipo'),
    path('equipos/editar/<int:pk>/', EditarEquipoView.as_view(), name='editar_equipo'),
    path('equipos/eliminar/<int:pk>', EliminarEquipoView.as_view(), name='eliminar_equipo'),

    # Formaciones
    path('formaciones/crear', CrearFormacionView.as_view(), name='crear_formacion'),
    path('formaciones/editar/<int:pk>', EditarFormacionView.as_view(), name='editar_formacion'),
    path('formaciones/eliminar/<int:pk>', EliminarFormacionView.as_view(), name='eliminar_formacion'),

    # Empleados (Plantel Técnico)
    path('empleados/crear', CrearEmpleadoView.as_view(), name='crear_empleado'),
    path('empleados/editar/<int:pk>/', EditarEmpleadoView.as_view(), name='editar_empleado'),
    path('empleados/eliminar/<int:pk>', EliminarEmpleadoView.as_view(), name='eliminar_empleado'),
]

handler404 = Error404View.as_view()
