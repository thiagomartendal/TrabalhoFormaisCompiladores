from .classes.Estado import Estado
from .classes.Automato import Automato
from .classes.Transicao import Transicao
from .classes.Gramatica import Gramatica
from .classes.ListaDeItens import ListaDeItens
import pickle

listaItens = ListaDeItens()

def estadosAutomato(request):
    if request.method == 'POST':
        global listaItens
        totalEstados = int(request.POST['num_vals'])
        nomeAutomato = request.POST['nome_automato']
        simbolosAlfabeto = request.POST['simbolos_alfabeto']
        simbolosAlfabeto.replace(" ", "")
        estados = []
        for i in range(1, totalEstados+1):
            nomeEstado = request.POST['nome_estado%d' % i]
            tipo = int(request.POST['tipo_estado%d' % i])
            estado = Estado(nomeEstado, tipo)
            estados.append(estado)
        automato = Automato(nomeAutomato)
        automato.setSimbolos(simbolosAlfabeto.split(","))
        automato.setEstados(estados)
        # salvar(automato)
        global listaItens
        listaItens.adicionaItem(automato)

def aplicarEdicaoAutomato(request):
    if request.method == 'POST':
        global listaItens
        posicao = int(request.GET['pos'])
        totalVals = int(request.POST['totalVals'])
        totalSimbolos = int(request.POST['total_simbolos'])
        simbolosAlfabeto = request.POST['simbolos_alfabeto']
        simbolos = simbolosAlfabeto.split(",")
        automato = listaItens.getItem(posicao)
        automato.setSimbolos(simbolos)
        for i in range(1, totalVals+1):
            nomeEstadoPartida = request.POST['nome_estado%d' % i]
            estadosChegada = request.POST['estado_chegada%d' % i]
            if estadosChegada != "":
                chegada = estadosChegada.split(",")
                listaEstados = []
                for c in chegada:
                    tmp = automato.procurarEstado(c)
                    listaEstados.append(tmp)

def formarGramatica(request):
    if request.method == 'POST':
        global listaItens
        nomeGramatica = request.POST['nome_gramatica']
        textoGramatica = request.POST['entrada_gramatica']
        gramatica = Gramatica(nomeGramatica)
        gramatica.parse(textoGramatica)
        listaItens.adicionaItem(gramatica)

def aplicarEdicaoGramatica(request):
    if request.method == 'POST':
        global listaItens
        posicao = int(request.GET['pos'])
        nomeGramatica = request.POST['nome_gramatica']
        textoGramatica = request.POST['entrada_gramatica']
        gramatica = listaItens.getItem(posicao)
        gramatica.set_nome(nomeGramatica)
        gramatica.parse(textoGramatica)
        listaItens.getLista()[posicao] = gramatica

def salvar(obj):
    with open('objetos.pkl', 'wb') as output:
        pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)
