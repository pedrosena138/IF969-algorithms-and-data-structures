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
    
    def Pesquisar(self, item):
        if self.Vazia():
            return False
        else:
            no = self.__raiz
            if item > no.getItem():
                filho_direita = no.getFilhoDireita()
                return filho_direita.Pesquisar(item)
            elif item < self.__raiz.getItem():
                filho_esquerda = no.getFilhoEsquerda()
                return filho_esquerda.Pesquisar(item)
            else:
                return no.getItem()

    def Inserir(self, item):
        novo_no = No(item)
        if self.Vazia():
            self.__raiz = novo_no
            self.__raiz.setFilhoDireita(ArvoreBinaria())
            self.__raiz.setFilhoEsquerda(ArvoreBinaria())
        else:
            no = self.__raiz
            if item > no.getItem():
                filho_direita = no.getFilhoDireita()
                filho_direita.Inserir(item)
            elif item < self.__raiz.getItem():
                filho_esquerda = no.getFilhoEsquerda()
                filho_esquerda.Inserir(item)
            else:
                raise ValueError('Valor já existente na arvore')
    
    def __str__(self):
        return str(self.__raiz.getFilhoDireita().__raiz)
            
def main():
    arvore = ArvoreBinaria()
    arvore.Inserir(5)
    arvore.Inserir(3)
    arvore.Inserir(8)
    arvore.Inserir(4)
    arvore.Inserir(6)
    print(arvore.Pesquisar(7))
    print(arvore)

if __name__ == "__main__":
    main()