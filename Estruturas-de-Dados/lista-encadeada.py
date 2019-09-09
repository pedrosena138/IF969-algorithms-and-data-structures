'''
Universidade Federal de Pernambuco - UFPE (www.ufpe.br)
Centro de Informática - CIn (www2.cin.ufpe.br) 
Bacharelado em Sistemas de Informação 
IF969 - Algoritmos e Estrutura de Dados 
Professor: Hansenclever Bassani 
Autor: Pedro Manoel Farias Sena de Lima (pmfsl)
Email: pmfsl@cin.ufpe.br
Data:
Copyright © 2019 todos os direitos reservados
Descricao: Implementacao de uma estrutura de dados tipo Lista Encadeada.
'''

class No:
    '''
    Implementacao do no da lista
    '''
    def __init__(self):
        self.__valor = None
        self.__proximo = None
    
    #Get e Set de valor
    def getValor(self):
        return self.__valor
    def setValor(self, novo_valor):
        self.__valor = novo_valor

    #Get e Set de proximo
    def getProximo(self):
        return self.__proximo
    def setProximo(self, novo_proximo):
        self.__proximo = novo_proximo
    
    def __str__(self):
        return str(self.__valor)

class ListaEncadeada:
    '''
    Implementacao de uma lista encadeada
    '''
    def __init__(self):
        self.__comeco = None
    
    def Vazia(self):
        '''
        Retorna True se a lista estiver vazia
        '''
        return self.__comeco is None
    
    def Inserir(self, valor):
        '''
        Insere um item na lista
        '''
        if self.Vazia():
            self.__comeco = No()
            self.__comeco.setValor(valor)
        else:
            novo_no = No()
            novo_no.setValor(valor)
            novo_no.setProximo(self.__comeco)
            self.__comeco = novo_no
    
    def __str__(self):
        return str(self.__comeco)

def main():
    lista = ListaEncadeada()
    lista.Inserir(78)
    lista.Inserir(45)
    lista.Inserir(98)
    print(lista.Vazia())
    print(lista)

if __name__ == "__main__":
    main()
