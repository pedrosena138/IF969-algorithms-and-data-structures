"""
Universidade Federal de Pernambuco - UFPE (www.ufpe.br)
Centro de Informática - CIn (www2.cin.ufpe.br) 
Bacharelado em Sistemas de Informação  
Autor: Pedro Manoel Farias Sena de Lima (pmfsl)
Email: pmfsl@cin.ufpe.br
Data: 2019-09-30
Copyright © 2019 todos os direitos reservados
Descricao: Implementacao de um no da arvore.
"""

class No():
    '''
    Implementacao do no da arvore
    '''
    def __init__(self, chave, valor):
        self.__chave = chave
        self.__valor = valor
        self.__filhoDireita = None
        self.__filhoEsquerda = None
    
    #Get de chave
    def getChave(self):
        return self.__chave

    #Get e Set de valor
    def getValor(self):
        return self.__valor
    def setValor(self, novo_valor):
        self.__valor = novo_valor
    
    #Get e Set do filho da direita
    def getFilhoDireita(self):
        return self.__filhoDireita
    def setFilhoDireita(self, novo_filho):
        self.__filhoDireita = novo_filho
    
    #Get e Set do filho da esquerda
    def getFilhoEsquerda(self):
        return self.__filhoEsquerda
    def setFilhoEsquerda(self, novo_filho):
        self.__filhoEsquerda = novo_filho
    
    def getTipo(self, no):
        '''
        Verifica se o tipo do objeto e o mesmo
        '''
        if type(self) == type(no):
            return True
        else:
            raise TypeError('Tipos diferentes de objetos')

    def __str__(self):
        return str(self.__valor)
    def __repr__(self):
        no = self.__valor
        return str(no)
    
    #Metodos comparativos
    def __lt__(self, no):
        if self.getTipo(no):
            return self.__valor < no.getValor()

    def __gt__(self, no):
        if self.getTipo(no):
            return self.__valor > no.getValor()
    
    def __le__(self, no):
        if self.getTipo(no):
            return self.__valor <= no.getValor()
    
    def __ge__(self, no):
        if self.getTipo(no):
            return self.__valor >= no.getValor()
    
    def __eq__(self, no):
        if self.getTipo(no):
            return self.__valor == no.getValor()
    
    def __ne__(self, no):
        if self.getTipo(no):
            return self.__valor != no.getValor()