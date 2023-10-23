from django.urls import path
from organizacion_mundial import views

urlpatterns = [
    path('', views.index, name=''),
    path('mundiales/',views.mundiales, name='mundiales'),
    path('fases/', views.fases, name='fases')
]