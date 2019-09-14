'''
Universidade Federal de Pernambuco - UFPE (www.ufpe.br)
Centro de Informática - CIn (www2.cin.ufpe.br) 
Bacharelado em Sistemas de Informação 
IF969 - Algoritmos e Estrutura de Dados 
Professor: Hansenclever Bassani 
Autor: Pedro Manoel Farias Sena de Lima (pmfsl)
Email: pmfsl@cin.ufpe.br
Data: 2019-09-14
Copyright © 2019 todos os direitos reservados
Descricao: Implementacao de uma estrutura de dados tipo Lista Duplamente Ligada.
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
    def __init__(self,item=None):
        self.__comeco = None
        self.__fim = None
        self.__item = item

        if not(self.__item is None):
            for i in item:
                self.Anexar(i)
    
    def Vazia(self):
        '''
        Retorna True se a lista estiver vazia
        '''
        return self.__comeco is None
    
    def Indice(self, item):
        '''
        Proucura um iem na lista e retorna seu indice ou um erro caso o itme nao esteja na lista
        '''
        if self.Vazia():
            raise ValueError('Lista-Dupla-Ligada.Indice(x): x nao esta na lista')
        else:
            no = self.__comeco
            no_achado = False
            indice = int()
            while not(no is None) and not(no_achado):
                if no.getValor() == item:
                    no_achado = True
                else:
                    no = no.getProximo()
                    indice += 1
            if no_achado:    
                return indice
            else:
                raise ValueError('Lista-Dupla-Ligada.Indice(x): x nao esta na lista')
    
    def Anexar(self, item):
        '''
        Insere um item no final da lista
        '''
        novo_no = No(item)
        if self.Vazia():
            self.__comeco = self.__fim = novo_no
        else:
            self.__fim.setProximo(novo_no)
            novo_no.setAnterior(self.__fim)
            self.__fim = novo_no
        
    def Inserir(self, chave, item):
        '''
        Insere um item de forma ordenada na lista
        '''
        novo_no = No(item)
        no_antigo = self.__getitem__(chave)

        if no_antigo == self.__comeco:
            novo_no.setProximo(no_antigo)
            no_antigo.setAnterior(novo_no)
            self.__comeco = novo_no
        else:
            no_anterior = no_antigo.getAnterior()
            no_antigo.setAnterior(novo_no)
            no_anterior.setProximo(novo_no)
            novo_no.setProximo(no_antigo)
            novo_no.setAnterior(no_anterior)
    
    def Concatenar(self, outro):
        if type(outro) != type(self):
            raise TypeError("operacao invalida: valor deve ser 'ListaDupla()'")
        else:
            for no in outro:
                self.Anexar(no)
            
            outro.Apagar()
                
    def Apagar(self):
        while not(self.Vazia()):
            no_proximo = self.__comeco.getProximo()
            if not(no_proximo is None): no_proximo.setAnterior(None)
            self.__comeco.setProximo(None)
            self.__comeco = no_proximo

    def Selecionar(self, item):
        '''
        Seleciona um no para ser removido da lista, retorna o valor desse no
        '''
        indice_remover = self.Indice(item)
        no_remover = self[indice_remover]
        no_proximo = no_remover.getProximo()
        no_anterior = no_remover.getAnterior()

        if no_remover == self.__comeco:
            no_remover.setProximo(None)
            no_proximo.setAnterior(None)
            self.__comeco = no_proximo
        elif no_remover == self.__fim:
            no_remover.setAnterior(None)
            no_anterior.setProximo(None)
            self.__fim = no_anterior
        else:    
            no_remover.setProximo(None)
            no_remover.setAnterior(None)

            no_anterior.setProximo(no_proximo)
            no_proximo.setAnterior(no_anterior)
        
        return item
    
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
    
    def __setitem__(self, chave, valor):
        '''
        Atualiza o valor de um no
        '''
        no = self.__getitem__(chave)
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
        return ('ListaDuplaLigada(%s)' % self.__str__())

'''
def main():
    lista1 = ListaDupla('algoritmos')
    lista2 = ListaDupla('lista')
    print('Lista 1:',lista1)
    print('Lista 2:',lista2)
    
    lista1.Anexar(1)
    lista2.Inserir(1,'O')
    print('\nLista 1:',lista1)
    print('Lista 2:',lista2)
    
    print("\nIndice do 'g' na Lista 1:",lista1.Indice('g'))
    print("Indice do 'O' na Lista 2:",lista2.Indice('O'))
    
    lista1[0] = 'A'
    lista2[0] = 'L'
    print('\nLista 1:',lista1)
    print('Lista 2:',lista2)
    
    print("\nRemover o {} da Lista 1" .format(lista1.Selecionar(1)))
    print("Remover o {} da Lista 2" .format(lista2.Selecionar('O')))
    print('\nLista 1:',lista1)
    print('Lista 2:',lista2)
    
    print('\nA Lista 1 tem {} elemento(s)' .format(len(lista1)))
    print('A Lista 2 tem {} elemento(s)' .format(len(lista2)))

    lista1.Concatenar(lista2)
    print('\nLista 1:',lista1)
    print('Lista 2:',lista2)
    
if __name__ == "__main__":
    main()
'''