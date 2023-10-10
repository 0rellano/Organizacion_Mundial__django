from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, DetailView
from .models import Pais

def index(request):
    return render(request, 'index.html')

class ListaPaises(ListView):
    model = Pais
    context_object_name = 'paises'
    template_name = 'paises.html'
    
class PaisView(DetailView):
    model = Pais
    context_object_name = 'pais'
    template_name = 'pais.html'
    pk_url_kwarg = 'pk'
