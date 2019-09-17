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
        self.__anterior = None
    
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
    
    #Get e Set do no anterior
    def getAnterior(self):
        return self.__anterior
    def setAnterior(self, no_anterior):
        self.__anterior = no_anterior

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
    
    def Vazia(self):
        '''
        Retorna True se a arvore for vazia
        '''
        return self.__raiz is None
    
    def Inserir(self, item):
        if self.Vazia():
            novo_no = No(item)
            self.__raiz = novo_no
        else:
            no = self.__raiz
            if item > no.getItem():
                pass
            elif item < no.getItem():
            while not(no.getFilhoDireita() is None) and not(no.getFilhoEsquerda() is None):
                if item > no.getItem():
                    no = no.getFilhoDireita()
                elif item < no.getItem():
                    no = no.getFilhoEsquerda()

def main():
    arvore = ArvoreBinaria()
    arvore.Inserir(8)
    print(arvore.Vazia())
if __name__ == "__main__":
    main()