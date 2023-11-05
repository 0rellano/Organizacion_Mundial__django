from collections.abc import Mapping
from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.utils import ErrorList
from organizacion_mundial.models import Jugador, Pais, Equipo, Posicion
from django.forms.widgets import TextInput

class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name' , 'email', 'password1', 'password2']


class DateInput(TextInput):
    input_type = 'date'


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
        widget=DateInput(attrs={'class': 'form-control'}),
        input_formats=['%Y-%m-%d'],  # Agrega el formato aquí
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

class PaisForm(forms.ModelForm):
    class Meta:
        model = Pais
        fields = '__all__'
    
    nombre = forms.CharField(max_length=100
        , widget=forms.TextInput(attrs={
            'placeholder': 'Argentina',
        })
    )
    liga_nombre = forms.CharField(max_length=100
        , widget=forms.TextInput(attrs={
            'placeholder': 'Liga Profesional',
        })
    )


class PosicionForm(forms.ModelForm):
    class Meta:
        model = Posicion
        fields = '__all__'

    nombre_posicion = forms.CharField(max_length=100)


class PlantelForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = '__all__'

    nombre = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Argentina',
            'class': 'form-control',
        })
    )
    descripcion = forms.CharField(
        max_length=300,
        widget=forms.TextInput(attrs={
            'placeholder': 'Liga Profesional',
            'class': 'form-control',
        })
    )

    # Campos para un jugador del plantel
    jugador_nombre = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Lionel',
            'class': 'form-control',
        })
    )
    jugador_apellido = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Messi',
            'class': 'form-control',
        })
    )
    jugador_nro_pasaporte = forms.CharField(
        label="Número de Pasaporte",
        max_length=200,
        widget=forms.NumberInput(attrs={
            'placeholder': '123456789',
            'class': 'form-control',
        })
    )
    jugador_fecha_nacimiento = forms.DateField(
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date',
        })
    )
    jugador_numero_camiseta = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'placeholder': '10',
            'class': 'form-control',
        })
    )
    jugador_pais = forms.ModelChoiceField(
        queryset=Pais.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )
    jugador_posicion = forms.ModelChoiceField(
        queryset=Posicion.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )
    jugador_fecha_retiro = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date',
        })
    )