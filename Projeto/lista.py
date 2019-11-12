#-*- coding: utf-8 -*-
'''
Arquivo com a classe Lista() que armazena objetos e os organiza
'''

class No:
    '''
    Implementacao do no da lista
    '''
    def __init__(self, valor=None):
        self.__valor = valor
        self.__proximo = None
        self.__anterior = None
    
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
    
    #Get e Set de anterior
    def getAnterior(self):
        return self.__anterior
    def setAnterior(self, novo_anterior):
        self.__anterior = novo_anterior
    
    def __str__(self):
        return str(self.__valor)
    
    def __repr__(self):
        return self.__valor

class ListaDupla:
    '''
    Implementacao da lista duplamente ligada
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
    
    def Inserir(self, valor):
        '''
        Insere um item na lista
        '''
        novo_no = No(valor)
        if self.Vazia():
            self.__comeco = self.__fim = novo_no
        else:
           self.__fim.setProximo(novo_no)
           novo_no.setAnterior(self.__fim)
           self.__fim = novo_no
    
    def Remover(self,valor):
        if self.Vazia() or not(self.Pesquisar(valor)):
            raise ValueError('Lista.Remover(x): x nao esta na lista')
        else:
            no_atual = self.__comeco
            no_achado = False

            while not(no_achado):
                if no_atual.getValor() == valor:
                    no_achado = True
                else:
                    no_atual = no_atual.getProximo()
            
            no_anterior = no_atual.getAnterior()
            no_proximo = no_atual.getProximo()
            if self.__len__() == 1:
                self.__comeco = None
            else:
                if no_atual == self.__comeco:
                    no_atual.setProximo(None)
                    no_proximo.setAnterior(None)
                    self.__comeco = no_proximo
                elif no_atual == self.__fim:
                    no_atual.setAnterior(None)
                    no_anterior.setProximo(None)
                    self.__fim = no_anterior
                else:
                    no_atual.setProximo(None)
                    no_atual.setAnterior(None)
                    no_proximo.setAnterior(no_anterior)
                    no_anterior.setProximo(no_proximo)
    
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
    
    def __len__(self):
        '''
        Retorna a quantidade de itens na lista
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
        return ('Lista(%s)' % self.__str__())

if __name__ == "__main__":
    lista = ListaDupla()
    lista.Inserir(4)
    lista.Remover(4)
    print(lista)