from django import template
from compilador.classes.ListaDeItens import ListaDeItens
from compilador.classes.Item import Item, TipoItem
import os.path
import pickle

register = template.Library()
listaItens = ListaDeItens()

@register.simple_tag
def itensCriados():
    global listaItens
    nomes = []
    for i in range(len(listaItens.getLista())):
        item = listaItens.getLista()[i]
        tipo = None
        if item.get_tipo() == TipoItem.AF:
            tipo = 0
        elif item.get_tipo() == TipoItem.GR:
            tipo = 1
        else:
            tipo = 2
        nomes.append([item.get_nome(), tipo, i])
    return nomes

# @register.simple_tag
# def itensCriados():
#     tamanho = os.path.getsize("objetos.pkl")
#     if tamanho == 0:
#         return 0
#     else:
#         nomes = []
#         with open('objetos.pkl', 'rb') as input:
#             obj = pickle.load(input)
#             tipo = None
#             if obj.get_tipo() == TipoItem.AF:
#                 tipo = 0
#             elif obj.get_tipo() == TipoItem.GR:
#                 tipo = 1
#             else:
#                 tipo = 2
#             nomes.append([obj.get_nome(), tipo, -1])
#         return nomes

@register.simple_tag
def itemSelecionado(request):
    try:
        global listaItens
        posicao = request.GET['pos']
        item = listaItens.getItem(int(posicao))
        estados = []
        for estado in item.getEstados():
            estados.append([estado.getNome(), estado.getTipo()])
        simbolos = ""
        for i in range(len(item.getSimbolos())):
            simbolos += item.getSimbolos()[i]
            if i < len(item.getSimbolos())-1:
                simbolos += ','
        return [item.get_nome(), simbolos, estados, item.getSimbolos()]
    except IndexError:
        return 0

@register.simple_tag
def gramaticaSelecionada(request):
    try:
        global listaItens
        posicao = request.GET['pos']
        gramatica = listaItens.getItem(int(posicao))
        txt = ""
        dicionario = gramatica.getProducoes().items()
        for k, v in dicionario:
            txt += str(k)+"->"+str(v)+"\n"
        txt = txt.replace("[", "")
        txt = txt.replace("]", "")
        txt = txt.replace("'", "")
        txt = txt.replace(", ", "|")
        return [gramatica.get_nome(), txt]
    except IndexError:
        return 0
