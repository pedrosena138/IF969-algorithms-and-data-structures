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
    
    def __getTipo(self, no):
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
        return self.__valor
    
    #Metodos comparativos
    def __lt__(self, no):
        if self.__getTipo(no):
            return self.__valor < no.getValor()

    def __gt__(self, no):
        if self.__getTipo(no):
            return self.__valor > no.getValor()
    
    def __le__(self, no):
        if self.__getTipo(no):
            return self.__valor <= no.getValor()
    
    def __ge__(self, no):
        if self.__getTipo(no):
            return self.__valor >= no.getValor()
    
    def __eq__(self, no):
        if self.__getTipo(no):
            return self.__valor == no.getValor()
    
    def __ne__(self, no):
        if self.__getTipo(no):
            return self.__valor != no.getValor()

class Lista:
    '''
    Implementacao da lista duplamente ligada
    '''
    def __init__(self):
        self.__comeco = None
        self.__fim = None
    
    def __vazia(self):
        '''
        Retorna True se a lista estiver vazia
        '''
        return self.__comeco is None
    
    def Pesquisar(self, valor):
        '''
        Verifica se existe um no com o valor passado como parametro na lista.
        Retorna o retorna True se o no estiver na lista.
        '''
        if self.__vazia():
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
        if self.__vazia():
            self.__comeco = self.__fim = novo_no
        else:
            if novo_no >= self.__fim:
                self.__fim.setProximo(novo_no)
                novo_no.setAnterior(self.__fim)
                novo_no.setProximo(None)
                self.__fim = novo_no
            elif novo_no <= self.__comeco:
                self.__comeco.setAnterior(novo_no)
                novo_no.setProximo(self.__comeco)
                self.__comeco = novo_no
            else:
                no_atual = self.__comeco
                no_proximo = self.__comeco.getProximo()
                while not(no_proximo is None) and novo_no >= no_proximo:
                    no_atual = no_proximo
                    no_proximo = no_atual.getProximo()
                no_atual.setProximo(novo_no)
                novo_no.setAnterior(no_atual)
                novo_no.setProximo(no_proximo)

    def Remover(self,valor):
        '''
        Remove um item da lista
        '''
        if self.__vazia() or not(self.Pesquisar(valor)):
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
    
    def Comparar(self, valor1, valor2):
        if self.__vazia() or not(self.Pesquisar(valor1) or self.Pesquisar(valor2)):
            raise IndexError('indice(s) fora da lista')
        else:
            if valor1 < valor2:
                return -1
            elif valor1 == valor2:
                return 0
            elif valor1 > valor2:
                return 1

    def __getitem__(self, chave):
        '''
        Retorna o valor do no que contem a chave passada como parametro
        '''
        indice = self.__len__()-1
        if (chave > indice) or (self.__vazia()):
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
        if self.__vazia():
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
        self.Remover(no.getValor())
        self.Inserir(valor)

    def __str__(self):
        '''
        Retorna uma representacao em forma de string do objeto
        '''
        if self.__vazia():
            return '[]'
        else:
            saida = str()
            saida += '['

            for no in self:
                if no.getProximo() is None:
                    saida += str(no) + ']'
                else:
                    saida += str(no) + ', '
            return saida

    def __repr__(self):
        return ('Lista(%s)' % self.__str__())