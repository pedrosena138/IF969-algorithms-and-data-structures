"""
Universidade Federal de Pernambuco - UFPE (www.ufpe.br)
Centro de Informática - CIn (www2.cin.ufpe.br) 
Bacharelado em Sistemas de Informação  
Autor: Pedro Manoel Farias Sena de Lima (pmfsl)
Email: pmfsl@cin.ufpe.br
Data: 2019-09-12
Copyright © 2019 todos os direitos reservados
Descricao: Implementacao de uma estrutura de dados tipo Arvore Binaria de Busca.
"""

class No():
    '''
    Implementacao do no da arvore
    '''
    def __init__(self, item=None):
        self.__item = item
        self.__filhoDireita = None
        self.__filhoEsquerda = None
        self.__pai = None
    
    #Get e Set de valor
    def getItem(self):
        return self.__item
    def setItem(self, novo_item):
        self.__item = novo_item
    
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

    #Get e Set do no pai
    def getPai(self):
        return self.__pai
    def setPai(self, no_pai):
        self.__pai = no_pai

    def __str__(self):
        return str(self.__item)
    def __repr__(self):
        no = self.__item
        return 'No(%s)' % str(no)

class ArvoreBinaria():
    def __init__(self):
        '''
        Metodo construtor da arvore
        '''
        self.__raiz = None
    
    def getRaiz(self):
        return self.__raiz

    def Vazia(self):
        '''
        Retorna True se a arvore for vazia
        '''
        return self.__raiz is None
    
    def Inserir(self, item):
        novo_no = No(item)
        if self.Vazia():
            self.__raiz = novo_no
        else:
            no_atual = self.__raiz
            while True:
                no_pai = no_atual
                if item < no_atual.getItem():
                    #inserir a esquerda
                    no_atual = no_atual.getFilhoEsquerda()
                    if no_atual is None:
                        no_pai.setFilhoDireita(novo_no)
                        novo_no.setPai(no_pai)
                        return
                elif item > no_atual.getItem():
                    #inserir na direita
                    no_atual = no_atual.getFilhoDireita()
                    if no_atual is None:
                        no_pai.setFilhoDireita(novo_no)
                        novo_no.setPai(no_pai)
                        return
                else:
                    raise ValueError('No já existente na arvore')
    
    def preOrdem(self, no):
        if not(no is None):
            print(no.getItem(),end=" ")
            self.emOrdem(no.getFilhoEsquerda())
            self.emOrdem(no.getFilhoDireita())
    
    def emOrdem(self, no):
        if not(no is None):
            self.emOrdem(no.getFilhoEsquerda())
            print(no.getItem(),end=" ")
            self.emOrdem(no.getFilhoDireita())
    
    def posOrdem(self, no):
        if not(no is None):
            self.emOrdem(no.getFilhoEsquerda())
            self.emOrdem(no.getFilhoDireita())
            print(no.getItem(),end=" ")

def main():
    arvore = ArvoreBinaria()
    arvore.Inserir(8)
    arvore.Inserir(3)
    arvore.Inserir(10)

    raiz = arvore.getRaiz()
    arvore.emOrdem(raiz)

if __name__ == "__main__":
    main()