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
        self.__filho_direita = None
        self.__filho_esquerda = None
    
    #Get e Set de valor
    def getItem(self):
        return self.__item
    def setItem(self, novo_item):
        self.__item = novo_item
    
    #Get e Set do filho da direita
    def getFilhoDireita(self):
        return self.__filho_direita
    def setFilhoDireita(self, novo_filho):
        self.__filho_direita = novo_filho
    
    #Get e Set do filho da esquerda
    def getFilhoEsquerda(self):
        return self.__filho_esquerda
    def setFilhoEsquerda(self, novo_filho):
        self.__filho_esquerda = novo_filho

    def __str__(self):
        return str(self.__item)
    def __repr__(self):
        no = self.__item
        return 'No(%s)' % str(no)

class ArvoreAVL():
    def __init__(self):
        '''
        Metodo construtor da arvore
        '''
        self.__raiz = None
        self.__altura = -1
        self.__balanco = 0
    
    def Altura(self):
        '''
        Metodo que retorna o tamanho da arvore
        '''
        if self.__raiz is not None:
            return self.__altura
        else:
            return 0
    
    def Folha(self):
        '''
        Metodo que retorna True se o no for uma folha
        '''
        return (self.__altura == 0)
    
    def Inserir(self, item):
        '''
        Insere um no na arvore
        '''
        novo_no = No(item)
        arvore = self.__raiz

        if arvore is None:
            self.__raiz = novo_no
            self.__raiz.setFilhoEsquerda(ArvoreAVL())
            self.__raiz.setFilhoDireita(ArvoreAVL())
        elif item < arvore.getItem():
            arvore_esquerda = self.__raiz.getFilhoEsquerda()
            arvore_esquerda.Inserir(item)
        elif item > arvore.getItem():
            arvore_direita = self.__raiz.getFilhoDireita()
            arvore_direita.Inserir(item)
        else:
            raise ValueError('No já existente na arvore')

    def __str__(self):
        return str(self.__raiz)

def main():
    arvore = ArvoreAVL()
    arvore.Inserir(8)
    arvore.Inserir(4)
    print(arvore)

if __name__ == "__main__":
    main()