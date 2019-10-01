"""
Universidade Federal de Pernambuco - UFPE (www.ufpe.br)
Centro de Informática - CIn (www2.cin.ufpe.br) 
Bacharelado em Sistemas de Informação  
Autor: Pedro Manoel Farias Sena de Lima (pmfsl)
Email: pmfsl@cin.ufpe.br
Data: 2019-09-30
Copyright © 2019 todos os direitos reservados
Descricao: Implementacao de uma Arvore Binaria de Busca.
"""

class No():
    '''
    Implementacao do no da arvore
    '''
    def __init__(self, chave, valor):
        self.__chave = chave
        self.__valor = valor
        self.__filhoDireita = None
        self.__filhoEsquerda = None
    
    #Get de chave
    def getChave(self):
        return self.__chave

    #Get e Set de valor
    def getValor(self):
        return self.__valor
    def setValor(self, novo_valor):
        self.__valor = novo_valor
    
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
    
    def getTipo(self, no):
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
        no = self.__valor
        return str(no)
    
    #Metodos comparativos
    def __lt__(self, no):
        if self.getTipo(no):
            return self.__valor < no.getValor()

    def __gt__(self, no):
        if self.getTipo(no):
            return self.__valor > no.getValor()
    
    def __le__(self, no):
        if self.getTipo(no):
            return self.__valor <= no.getValor()
    
    def __ge__(self, no):
        if self.getTipo(no):
            return self.__valor >= no.getValor()
    
    def __eq__(self, no):
        if self.getTipo(no):
            return self.__valor == no.getValor()
    
    def __ne__(self, no):
        if self.getTipo(no):
            return self.__valor != no.getValor()

class ArvoreBinariaBusca():
    def __init__(self):
        '''
        Metodo construtor da arvore
        '''
        self.__raiz = None
        self.__altura = -1
    
    def __vazia(self):
        '''
        Retorna True se a arvore for vazia
        '''
        return self.__raiz is None
    
    def __procurar(self, chave):
        '''
        Proucura um no na arvore pela sua chave e retorna seu valor ou um erro caso o item nao esteja na arvore
        '''
        if self.__vazia():
            return False
        else:
            no = self.__raiz
            filho_direita = no.getFilhoDireita()
            filho_esquerda = no.getFilhoEsquerda()
            if chave > no.getChave():
                return filho_direita.__procurar(chave)
            elif chave < no.getChave():
                return filho_esquerda.__procurar(chave)
            elif chave == no.getChave():
                return no
            else:
                return False
    
    def __inserir(self, chave, item):
        '''
        Insere um novo no na arvore
        '''
        novo_no = No(chave, item)
        if self.__vazia():
            self.__raiz = novo_no
            novo_no.setFilhoDireita(ArvoreBinariaBusca())
            novo_no.setFilhoEsquerda(ArvoreBinariaBusca())
        else:
            no = self.__raiz
            if chave > no.getChave():
                filho_direita = no.getFilhoDireita()
                filho_direita.__inserir(chave, item)
            elif chave < no.getChave():
                filho_esquerda = no.getFilhoEsquerda()
                filho_esquerda.__inserir(chave, item)
            else:
                raise ValueError('Valor já existente na arvore')
    
    def __antecessor(self, raiz):
        '''
        Encontra filho mais a direita da sub-arvore da esquerda
        '''
        raiz = raiz.getFilhoEsquerda().__raiz
        if raiz is  not None:
            while raiz.getFilhoDireita() is not None:
                if raiz.getFilhoDireita().__raiz is None:
                    return raiz
                else:
                    raiz = raiz.getFilhoDireita().__raiz
        return raiz
            
    def __sucessor(self,raiz):
        '''
        Encontra o filho mais a esquerda da sub-arvore da direita
        '''
        raiz = raiz.getFilhoDireita().__raiz
        if raiz is not None:
            while raiz.getFilhoEsquerda() is not None:
                if raiz.getFilhoEsquerda().__raiz is None:
                    return raiz
                else:
                    raiz = raiz.getFilhoEsquerda().__raiz
        return raiz

    def __remover(self, chave):
        '''
        Remove um no na arvore e insere seu sucessor imediato
        '''
        if not(self.__vazia()):
            if self.__raiz.getChave() == chave:
                # caso a arvore nao tenha filhos
                if self.__raiz.getFilhoEsquerda().__raiz is None and self.__raiz.getFilhoDireita().__raiz is None:
                    self.__raiz = None
                #caso a arvore nao tenha filho a esquerda
                elif self.__raiz.getFilhoEsquerda().__raiz is None:
                    self.__raiz = self.__raiz.getFilhoDireita().__raiz
                #caso a arvore nao tenha filho a direita
                elif self.__raiz.getFilhoDireita().__raiz is None:
                    self.__raiz = self.__raiz.getFilhoEsquerda().__raiz
                #pior caso: possui ambos os filhos. Tem que encontrar o sucessor.
                else:
                    substituto = self.__sucessor(self.__raiz)
                    if substituto is not None:
                        self.__raiz.setItem(substituto)
                        self.__raiz.getFilhoDireita().__remover(substituto)
                return 
            elif chave < self.__raiz.getChave():
                self.__raiz.getFilhoEsquerda().__remover(chave)
            elif chave > self.__raiz.getChave():
                self.__raiz.getFilhoDireita().__remover(chave)
        else:
            return
    def preOrdem(self):
        '''
        Encaminhamento em pre ordem: raiz, filho da esquerda, filho da direita
        '''
        if self.__vazia():
            return []
        else:
            lista_saida = list()
            lista_saida.append(self.__raiz)

            esquerda = self.__raiz.getFilhoEsquerda().preOrdem()
            for no in esquerda:
                lista_saida.append(no)

            direita = self.__raiz.getFilhoDireita().preOrdem()
            for no in direita:
                lista_saida.append(no)

            return lista_saida
    
    def emOrdem(self):
        '''
        Encaminhamento em ordem: filho da esquerda, raiz, filho da direita
        '''
        if self.__vazia():
            return []
        else:
            lista_saida = list()
            esquerda = self.__raiz.getFilhoEsquerda().emOrdem()
            for no in esquerda:
                lista_saida.append(no)
            
            lista_saida.append(self.__raiz.getValor())

            direita = self.__raiz.getFilhoDireita().emOrdem()
            for no in direita:
                lista_saida.append(no)

            return lista_saida
    
    def posOrdem(self):
        '''
        Encaminhamento em pos ordem: filho da esquerda, filho da direita, raiz
        '''
        if self.__vazia():
            return []
        else:
            lista_saida = list()
           
            esquerda = self.__raiz.getFilhoEsquerda().posOrdem()
            for no in esquerda:
                lista_saida.append(no)

            direita = self.__raiz.getFilhoDireita().posOrdem()
            for no in direita:
                lista_saida.append(no)
            
            lista_saida.append(self.__raiz)

            return lista_saida
    
    def __bool__(self):
        '''
        Converte a arvore em valor booleano
        '''
        if self.__vazia():
            return False
        else:
            return True
   
    def __getitem__(self, chave):
        '''
        Retorna o valor contido na chave passada como parametro
        '''
        no =  self.__procurar(chave)
        return no
    
    def __setitem__(self, chave, valor):
        '''
        Atualiza o valor de um no se ele estiver na arvore.
        Se nao o insere
        '''
        no = self.__getitem__(chave)
        if  no:
            no.setValor(valor)
        else:
            self.__inserir(chave, valor)

    def __del__(self, chave):
        '''
        Remove um no da arvore com a chave passada como parametro
        '''

    def __iter__(self):
        '''
        Iterador da arvore
        '''
        self.__index = int()
        return self
    
    def __next__(self):
        '''
        Retorna o no correspondente ao iterador
        '''
        if self.__index < len(self.preOrdem()):
            no = self.preOrdem()[self.__index]
            self.__index += 1
            return no
        else:
            raise StopIteration

    def __str__(self):
        '''
        Representacao em str da arvore
        '''
        return str(self.emOrdem())
    
    def __repr(self):
        '''
        Representacao que pode ser instanciada da arvore
        '''
        return str(self.preOrdem())


arvore = ArvoreBinariaBusca()
arvore['a'] = 2
arvore['b'] = 1
print(arvore)
