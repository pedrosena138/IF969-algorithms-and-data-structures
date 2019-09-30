"""
Universidade Federal de Pernambuco - UFPE (www.ufpe.br)
Centro de Informática - CIn (www2.cin.ufpe.br) 
Bacharelado em Sistemas de Informação  
Autor: Pedro Manoel Farias Sena de Lima (pmfsl)
Email: pmfsl@cin.ufpe.br
Data: 2019-09-30
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
        return str(no)

class ArvoreBinaria():
    def __init__(self):
        '''
        Metodo construtor da arvore
        '''
        self.__raiz = None
        self.__altura = -1
    
    def __getAltura(self):
        '''
        Se a arvore for vaiza, sua alturae 0.
        Se nao, retorna sua altura
        '''
        if self.Vazia():
            return 0
        else:
            return self.__raiz.__altura
    
    def __setAltura(self, recursao=True):
        '''
        Atualiza a altura da arvore
        '''
        if not(self.Vazia()):
            filho_esquerda = self.__raiz.getFilhoEsquerda()
            filho_direita = self.__raiz.getFilhoDireita()
            if recursao:
                if filho_esquerda is not None:
                    filho_esquerda.__setAltura()
                if filho_direita is not None:
                    filho_direita.__setAltura()
            self.__altura = max(filho_direita.__altura,
                                filho_esquerda.__altura) + 1
        else:
            self.__altura = -1
    
    def Vazia(self):
        '''
        Retorna True se a arvore for vazia
        '''
        return self.__raiz is None
    
    def Pesquisar(self, item):
        '''
        Pesquisa um item na arvore.
        Retorna o item se ele estiver na arvore ou False se nao estiver.
        '''
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
        '''
        Insere um novo no na arvore
        '''
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
    
    def Antecessor(self, raiz):
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
            
    def Sucessor(self,raiz):
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
    
    def Remover(self, item):
        if not(self.Vazia()):
            if self.__raiz.getItem() == item:
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
                    substituto = self.Sucessor(self.__raiz)
                    if substituto is not None:
                        self.__raiz.setItem(substituto)
                        self.__raiz.getFilhoDireita().Remover(substituto)
                return 
            elif item < self.__raiz.getItem():
                self.__raiz.getFilhoEsquerda().Remover(item)
            elif item > self.__raiz.getItem():
                self.__raiz.getFilhoDireita().Remover(item)
        else:
            return

    def preOrdem(self):
        if self.Vazia():
            return []
        else:
            lista_saida = list()
            lista_saida.append(self.__raiz)

            esquerda = self.__raiz.getFilhoEsquerda().emOrdem()
            for no in esquerda:
                lista_saida.append(no)

            direita = self.__raiz.getFilhoDireita().emOrdem()
            for no in direita:
                lista_saida.append(no)

            return lista_saida
    
    def emOrdem(self):
        if self.Vazia():
            return []
        else:
            lista_saida = list()
            esquerda = self.__raiz.getFilhoEsquerda().emOrdem()
            for no in esquerda:
                lista_saida.append(no)
            
            lista_saida.append(self.__raiz)

            direita = self.__raiz.getFilhoDireita().emOrdem()
            for no in direita:
                lista_saida.append(no)

            return lista_saida
    
    def posOrdem(self):
        if self.Vazia():
            return []
        else:
            lista_saida = list()
           
            esquerda = self.__raiz.getFilhoEsquerda().emOrdem()
            for no in esquerda:
                lista_saida.append(no)

            direita = self.__raiz.getFilhoDireita().emOrdem()
            for no in direita:
                lista_saida.append(no)
            
            lista_saida.append(self.__raiz)

            return lista_saida
    
    def Imprimir(self, level=0, pref=''):
        self.__setAltura()
        if not(self.Vazia()):
            print (' ' * level * 2, pref, self.__raiz.getItem(), "[" + str(self.__altura) + "]")
            if self.__raiz.getFilhoEsquerda() is not None:
                self.__raiz.getFilhoEsquerda().Imprimir(level+1, '<')
            if self.__raiz.getFilhoEsquerda() is not None:
                self.__raiz.getFilhoDireita().Imprimir(level+1, '>')

    def __str__(self):
        return str(self.emOrdem())