from Estado import *
from Transicao import *
from Item import *

class Automato(Item):

    def __init__(self, nome):
        super(Automato, self).__init__(TipoItem.AF, nome)
        self.__estados = [] # Lista de estados, não é necessário classificar entre estado inicial e finais, pois o próprio estado já deve conhecer esta informação
        self.__transicoes = [] # Lista de transições

    # Adiciona um estado pronto
    def addEstado(self, estado):
        self.__estados.append(estado)

    # Cria um novo estado a partir de seus atributos, e o adiciona a lista de estados
    def formarEstado(self, nome, tipo):
        estado = Estado(nome, tipo)
        self.__estados.append(estado)

    # Define a lista de estados da classe com uma outra lista já existente
    def setEstados(self, estados):
        if estados is list:
            self.__estados = [x for x in estados]

    # Adiciona uma transição pronta
    def addTransicao(self, transicao):
        self.__transicoes.append(transicao)

    # Cria uma nova transição com seus parâmetros, e então adiciona a lista de transições
    def formarTransicao(self, estadoPartida, simbolo, estadosChegada):
        if estadosChegada is list:
            transicao = Transicao(estadoPartida, simbolo, estadosChegada)
            self.__transicoes.append(transicao)

    # Define a lista de transições da classe com uma outra lista já existente
    def setTransicoes(self, transicoes):
        if transicoes is list:
            self.__transicoes = [x for x in transicoes]
