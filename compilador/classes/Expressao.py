from Elemento import *

class Expressao(Elemento):

    def __init__(self, nome):
        super(Gramatica, self).__init__(TipoItem.ER, nome)