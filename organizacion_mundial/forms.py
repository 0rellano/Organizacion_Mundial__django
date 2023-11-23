from collections.abc import Mapping
from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.utils import ErrorList
from organizacion_mundial.models import Jugador, Pais, Equipo, Posicion, Mundial, Fase

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


class MundialForm(forms.ModelForm):
    class Meta:
        model = Mundial
        fields = '__all__'

    anio = forms.CharField(
         max_length=100,
         widget=forms.TextInput(attrs={
             'placeholder': '2026',
             'class': 'form-control',
         })
    )

    pais_sede = forms.ModelChoiceField(
         queryset=Pais.objects.all(),
         widget=forms.Select(attrs={
             'class': 'form-control'
         })
    )

    fecha_inicio = forms.DateField(
         widget=forms.DateInput(attrs={
              'class': 'form-control',
              'type': 'date',
              })
    )
    fecha_final = forms.DateField(
         widget=forms.DateInput(attrs={
              'class': 'form-control',
              'type': 'date',
              })
    )


class FaseForm(forms.ModelForm):
    class Meta:
        model = Fase
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        pk_mundial = self.initial.get('mundial')

        mundial = Mundial.objects.filter(pk=pk_mundial)
        print(mundial)
        if mundial:
            print('*0'*50)
            fecha_min = mundial.first().fecha_inicio
            fecha_max = mundial.first().fecha_final

            self.fields['fecha_inicio'].widget.attrs['min'] = fecha_min
            self.fields['fecha_inicio'].widget.attrs['max'] = fecha_max
            self.fields['fecha_final'].widget.attrs['min'] = fecha_min
            self.fields['fecha_final'].widget.attrs['max'] = fecha_max

        if pk_mundial:
            self.fields['mundial'].queryset = Mundial.objects.filter(pk=pk_mundial)
        else:
            self.fields['mundial'].queryset = Mundial.objects.all()

    nombre = forms.CharField(max_length=100)
    descripcion = forms.CharField(
        max_length=300,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
        })
    )
    fecha_inicio = forms.DateField(
        widget=forms.DateInput(attrs={
              'class': 'form-control',
              'type': 'date',
              })
    )
    fecha_final = forms.DateField(
        widget=forms.DateInput(attrs={
              'type': 'date',
              })
    )
    orden = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'readonly': False
        })
    )
    mundial = forms.ModelChoiceField(
        queryset=None,
        widget=forms.Select(attrs={
            'readonly': False
        })
    )
    