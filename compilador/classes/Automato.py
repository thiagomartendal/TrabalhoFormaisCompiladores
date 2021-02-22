from .Estado import Estado
from .Transicao import Transicao
from .Item import Item, TipoItem

class Automato(Item):

    def __init__(self, nome):
        super(Automato, self).__init__(TipoItem.AF, nome)
        self.__simbolos = [] # Lista de simbolos do alfabeto
        self.__estados = [] # Lista de estados, não é necessário classificar entre estado inicial e finais, pois o próprio estado já deve conhecer esta informação
        self.__transicoes = [] # Lista de transições

    # Adiciona simbolo ao alfabeto
    def addSimbolo(self, simbolo):
        self.__simbolos.append(simbolo)

    # Adiciona uma lista de simbolos
    def setSimbolos(self, simbolos):
        if type(simbolos) is list:
            self.__simbolos.clear()
            self.__simbolos = [s for s in simbolos]

    # Retorna o alfabeto do automato
    def getSimbolos(self):
        return self.__simbolos

    # Adiciona um estado pronto
    def addEstado(self, estado):
        self.__estados.append(estado)

    # Cria um novo estado a partir de seus atributos, e o adiciona a lista de estados
    def formarEstado(self, nome, tipo):
        estado = Estado(nome, tipo)
        self.__estados.append(estado)

    # Define a lista de estados da classe com uma outra lista já existente
    def setEstados(self, estados):
        if type(estados) is list:
            self.__estados.clear()
            self.__estados = [x for x in estados]

    # Retorna os estados
    def getEstados(self):
        return self.__estados

    # Retorna um estado do automato pelo nome
    def procurarEstado(self, nomeEstado):
        for estado in self.__estados:
            if estado.getNome() == nomeEstado:
                return estado
        return None

    # Adiciona uma transição pronta
    def addTransicao(self, transicao):
        self.__transicoes.append(transicao)

    # Cria uma nova transição com seus parâmetros, e então adiciona a lista de transições
    def formarTransicao(self, estadoPartida, simbolo, estadosChegada):
        if type(estadosChegada) is list:
            transicao = Transicao(estadoPartida, simbolo, estadosChegada)
            self.__transicoes.append(transicao)

    # Define a lista de transições da classe com uma outra lista já existente
    def setTransicoes(self, transicoes):
        if type(transicoes) is list:
            self.__transicoes.clear()
            self.__transicoes = [x for x in transicoes]

    # Retorna a lista de transições
    def getTransicoes(self):
        return self.__transicoes
