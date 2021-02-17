from Elemento import *

class Gramatica(Elemento):

    def __init__(self, nome):
        super(Gramatica, self).__init__(TipoItem.GR, nome)
        self.__producoes = {}  # Dicionario de producoes
        self.__texto = None 
        self.__simbolo_inicial = None

    # Adiciona uma nova producao ao dicionario
    def adicionaProducao(self, simbolo, producao):
        self.__producoes[simbolo] = producao

    # Retorna o dicionario inteiro
    def getProducoes(self):
        return self.__producoes

    # Modifica o simbolo inicial da gramatica regular
    def setSimboloInicial(self, simbolo):
        self.setSimboloInicial(simbolo)

    # Gera a estrutura gramatica a partir do texto escrito pelo usuario
    def parse(self, texto):
        if not texto:
            print("Texto vazio")
            return
        self.__texto = texto.replace(" ", "")
        lista_de_linhas = self.__texto.splitlines()
        # criar uma funcao que analisa o texto
