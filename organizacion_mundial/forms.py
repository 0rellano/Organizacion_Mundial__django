from collections.abc import Mapping
from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.utils import ErrorList
from organizacion_mundial.models import Jugador, Pais, Equipo, Posicion

class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name' , 'email', 'password1', 'password2']


class JugadorForm(forms.ModelForm):
    class Meta:
        model = Jugador
        fields = '__all__'

    nombre = forms.CharField(
         max_length=100,
         widget=forms.TextInput(attrs={
             'placeholder': 'Lionel',
             'class': 'form-control',
         })
    )
    apellido = forms.CharField(max_length=100
        , widget=forms.TextInput(attrs={
            'placeholder': 'Messi',
        })
    )
    nro_pasaporte = forms.CharField(
        label="Numero de Pasaporte",
        max_length=200,
        widget=forms.NumberInput(attrs={
             'placeholder': '123456789',
             'class': 'form-control',
             })
    )
    fecha_nacimiento = forms.DateField(
         widget=forms.DateInput(attrs={
             'class': 'form-control',
             'type': 'date',
            #  'input_formats': ['%d-%m-%Y'] # no se porque no me ada :(
         })
    )
    numero_camiseta = forms.IntegerField(
         widget=forms.NumberInput(attrs={
             'placeholder': '123456789',
             'class': 'form-control',
             })
    )
    pais = forms.ModelChoiceField(
         queryset=Pais.objects.all(), 
         widget=forms.Select(attrs={
              'class': 'form-control'
              })
    )
    equipo = forms.ModelChoiceField(
         queryset=Equipo.objects.all(), 
         widget=forms.Select(attrs={
              'class': 'form-control'
              })
    )
    posicion = forms.ModelChoiceField(
         queryset=Posicion.objects.all(), 
         widget=forms.Select(attrs={
             'class': 'form-control'
             })
    )
    fecha_retiro = forms.DateField(
         required=False, 
         widget=forms.DateInput(attrs={
              'class': 'form-control',
              'type': 'date',
              })
    )
