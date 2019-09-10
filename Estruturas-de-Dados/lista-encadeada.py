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
    
    def __repr__(self):
        return self.__valor

class ListaEncadeada:
    '''
    Implementacao de uma lista encadeada
    '''
    def __init__(self):
        self.__comeco = None
        self.__fim = None
    
    def Vazia(self):
        '''
        Retorna True se a lista estiver vazia
        '''
        return self.__comeco is None
    
    def Pesquisar(self, valor):
        '''
        Verifica se existe um no com o valor passado como parametro na lista.
        Retorna o retorna True se o no estiver na lista.
        '''
        if self.Vazia():
            raise Exception('lista vazia')
        else:
            no = self.__comeco
            while not(no.getProximo() is None) and (no.getValor() != valor):
                no = no.getProximo()
            if no.getValor() == valor:
                return True
            else:
                return False


    def Inserir(self, valor):
        '''
        Insere um item na lista
        '''
        if self.Vazia():
            novo_no = No()
            novo_no.setValor(valor)
            self.__comeco = self.__fim = novo_no
        elif self.Pesquisar(valor):
            raise Exception('valor ja existente na lista', valor)
        else:
            novo_no = No()
            novo_no.setValor(valor)
            self.__fim.setProximo(novo_no)
            self.__fim = novo_no

    def Remover(self,valor):
        if self.Pesquisar(valor):
            if self.__comeco.getValor() == valor:
                proximo_no = self.__comeco.getProximo()
                self.__comeco.setProximo(None)
                self.__comeco = proximo_no
                return self.__comeco
            else:
                no = self.__comeco
                while not(no.getProximo() is None) and (no.getProximo().getValor() != valor):
                    no = no.getProximo()
                
                if no.getProximo() ==  self.__fim:
                     no.setProximo(None)
                     self.__fim = no
                     return self.__fim
                else:
                    proximo_no = no.getProximo()
                    no.setProximo(proximo_no.getProximo())
        else:
            raise KeyError('valor nao encontrado')
        
    def __str__(self):
        return str(self.__comeco.getProximo())

def main():
    lista = ListaEncadeada()
    lista.Inserir(2)
    lista.Inserir(3)
    lista.Inserir(4)
    lista.Remover(3)
    print(lista)

if __name__ == "__main__":
    main()
