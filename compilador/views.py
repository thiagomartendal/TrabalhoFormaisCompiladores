from django.shortcuts import render
from .tools import *

# Create your views here.

def index(request):
    if request.method == 'POST':
        if request.POST['novo_automato'] != "":
            estadosAutomato(request)
        if request.POST['nova_gramatica'] != "":
            formarGramatica(request)
    return render(request, 'paginas/index.html')

def editarAutomato(request):
    return render(request, 'paginas/editar_automato.html')

def editarGramatica(request):
    aplicarEdicaoGramatica(request)
    return render(request, 'paginas/editar_gramatica.html')
