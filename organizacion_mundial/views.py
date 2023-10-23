from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, 'index.html')

def mundiales(request):
    return render(request, 'mundiales.html')

def fases(request):
    return render(request, 'fases.html')