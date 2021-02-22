from .classes.Estado import Estado
from .classes.Automato import Automato
from .classes.Transicao import Transicao
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

def aplicarEdicao(request):
    if request.method == 'POST':
        global listaItens
        posicao = int(request.GET['pos'])
        totalVals = int(request.POST['totalVals'])
        totalSimbolos = int(request.POST['total_simbolos'])
        automato = listaItens.getItem(posicao)
        for i in range(1, totalVals+1):
            nomeEstadoPartida = request.POST['nome_estado%d' % i]
            estadosChegada = request.POST['estado_chegada%d' % i]


def salvar(obj):
    with open('objetos.pkl', 'wb') as output:
        pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)
