from collections.abc import Mapping
from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.utils import ErrorList
from organizacion_mundial.models import *
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
            'class': 'form-control',
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
             'placeholder': '10',
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
    
=======
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
        model = Personal
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


class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = '__all__'

    nombre = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Nombre del equipo',
            'class': 'form-control',
        })
    )
    descripcion = forms.CharField(
        max_length=300,
        widget=forms.Textarea(attrs={
            'placeholder': 'Descripción del equipo',
            'class': 'form-control',
        })
    )
    pais_perteneciente = forms.ModelChoiceField(
        queryset=Pais.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )

class FormacionForm(forms.ModelForm):
    class Meta:
        model = Formacion
        fields = '__all__'

    pais = forms.ModelChoiceField(
        queryset=Pais.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )
    esquema = forms.ChoiceField(
        choices=Formacion.FORMACION_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )
    titulares = forms.ModelMultipleChoiceField(
        queryset=Jugador.objects.all(),
        widget=forms.SelectMultiple(attrs={
            'class': 'form-control'
        })
    )
    suplentes = forms.ModelMultipleChoiceField(
        queryset=Jugador.objects.all(),
        widget=forms.SelectMultiple(attrs={
            'class': 'form-control'
        })
    )
    # Puedes agregar más campos según tu modelo

class PaisSelectWidget(forms.Select):
    def format_option_label(self, value):
        if value:
            pais = Pais.objects.get(pk=value)
            return str(getattr(pais, 'nombre', ''))
        return super().format_option_label(value)

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Personal
        fields = '__all__'

    nombre = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Nombre',
            'class': 'form-control',
        })
    )
    apellido = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Apellido',
            'class': 'form-control',
        })
    )
    nro_pasaporte = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={
            'placeholder': 'Número de Pasaporte',
            'class': 'form-control',
        })
    )
    fecha_comienzo = forms.DateField(
        widget=DateInput(attrs={'class': 'form-control', 'placeholder': 'Fecha de comienzo'}),
        input_formats=['%Y-%m-%d'],
    )
    fecha_fin = forms.DateField(
        widget=DateInput(attrs={'class': 'form-control', 'placeholder': 'Fecha de fin'}),
        input_formats=['%Y-%m-%d'],
        required=False,  # Indica que el campo no es obligatorio
    )
    pais_perteneciente = forms.ModelChoiceField(
        queryset=Pais.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form-control',
            'placeholder': 'Seleccione el país'
        }),
        initial=None,  # Establece el valor inicial en None
        empty_label=None,  # Elimina la etiqueta vacía predeterminada
    )
    rol = forms.ModelChoiceField(
        queryset=Rol.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form-control',
            'placeholder': 'Seleccione el rol'
        })
    )
    fecha_nacimiento = forms.DateField(
        widget=DateInput(attrs={'class': 'form-control', 'placeholder': 'Seleccione la fecha de nacimiento'}),
        input_formats=['%Y-%m-%d'],
        required=False,  # Indica que el campo no es obligatorio
        initial=None,  # Establece el valor inicial en None
    )

    def __init__(self, *args, **kwargs):
        super(EmpleadoForm, self).__init__(*args, **kwargs)
        self.fields['pais_perteneciente'].empty_label = "Seleccione el país"
        
        # Establece el valor inicial solo si existe y no es None
        initial_pais = getattr(self.instance, 'pais_perteneciente_id', None)
        if initial_pais is not None:
            self.fields['pais_perteneciente'].initial = initial_pais

