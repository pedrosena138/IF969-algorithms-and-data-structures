"""
Universidade Federal de Pernambuco - UFPE (www.ufpe.br)
Centro de Informática - CIn (www2.cin.ufpe.br) 
Bacharelado em Sistemas de Informação 
IF969 - Algoritmos e Estrutura de Dados 
Professor: Hansenclever Bassani 
Autor: Pedro Manoel Farias Sena de Lima (pmfsl)
Email: pmfsl@cin.ufpe.br
Data: 2019-09-14
Copyright © 2019 todos os direitos reservados
Descricao: Implementacao de uma estrutura de dados tipo Fila.
"""

class No:
    '''
    Implementacao do no da fila
    '''
    def __init__(self, valor=None):
        self.__valor = valor
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

class Fila:
    '''
    Implementacao de uma fila
    '''
    def __init__(self):
        self.__comeco = None
        self.__fim = None
    
    def Vazia(self):
        '''
        Retorna True se a fila estiver vazia
        '''
        return self.__comeco is None
    
    def Pesquisar(self, valor):
        '''
        Verifica se existe um no com o valor passado como parametro na fila.
        Retorna o retorna True se o no estiver na pilha.
        '''
        if self.Vazia():
            return False
        else:
            no = self.__comeco
            no_achado = False
            while not(no is None) and not(no_achado):
                if no.getValor() == valor:
                    no_achado = True
                else:
                    no = no.getProximo()
            return no_achado
        
    def Enqueue(self, valor):
        '''
        Insere um item na fila
        '''
        novo_no = No(valor)
        if self.Vazia():
            self.__comeco = self.__fim = novo_no
        else:
           self.__fim.setProximo(novo_no)
           self.__fim = novo_no

    def Dequeue(self):
        '''
        Remove o primeiro item adicionado na fila
        '''
        if not(self.Vazia()):
            proximo_no = self.__comeco.getProximo()
            self.__comeco.setProximo(None)
            self.__comeco = proximo_no
    
    def __len__(self):
        '''
        Retorna a quantidade de itens na fila
        '''
        if self.Vazia():
            return 0
        else:
            cont = int()
            no = self.__comeco

            while not(no is None):
                cont += 1
                no = no.getProximo()
            return cont
    
    def __iter__(self):
        '''
        Iterador da lista
        '''
        self.__index = int()
        return self
    
    def __next__(self):
        '''
        Retorna o no correspondente ao iterador
        '''
        if self.__index < self.__len__():
            no = self.__getitem__(self.__index)
            self.__index += 1
            return no
        else:
            raise StopIteration
        
    def __getitem__(self, chave):
        '''
        Retorna o valor do no que contem a chave passada como parametro
        '''
        indice = self.__len__()-1
        if (chave > indice) or (self.Vazia()):
            raise IndexError('indice fora do alcance')
        else:
            no = self.__comeco
            cont = 0
            while cont < chave:
                no = no.getProximo()
                cont += 1
            return no
    
    def __setitem__(self, indice, valor):
        '''
        Atualiza o valor de um no
        '''
        no = self.__getitem__(indice)
        no.setValor(valor)

    def __str__(self):
        '''
        Retorna uma representacao em forma de string do objeto
        '''
        if self.Vazia():
            return '[]'
        else:
            saida = str()
            saida += '['

            for no in self:
                if no == self.__fim:
                    saida += str(no) + ']'
                else:
                    saida += str(no) + ', '
            return saida
    
    def __repr__(self):
        return ('Fila(%s)' % self.__str__())
