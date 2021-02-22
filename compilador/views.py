from django.shortcuts import render
from .tools import *

# Create your views here.

def index(request):
    estadosAutomato(request)
    return render(request, 'paginas/index.html')

def editarAutomato(request):
    return render(request, 'paginas/editar_automato.html')
