"""
Universidade Federal de Pernambuco - UFPE (www.ufpe.br)
Centro de Informática - CIn (www2.cin.ufpe.br) 
Bacharelado em Sistemas de Informação  
Autor: Pedro Manoel Farias Sena de Lima (pmfsl)
Email: pmfsl@cin.ufpe.br
Data: 2019-10-02
Copyright © 2019 todos os direitos reservados
Descricao: Implementacao de uma Arvore AVL.
"""

from random import randint, randrange
from questao01 import No, ArvoreBinariaBusca

class ArvoreAVL(ArvoreBinariaBusca):
    #Metodo construtor
    def __init__(self):
        '''
        Metodo construtor da arvore
        '''
        super().__init__()
        self.__altura = -1
        self.__balanco = 0
    #Metodos privados
    def __vazia(self):
        '''
        Retorna True se a arvore for vazia
        '''
        return super().__vazia()
    #|- Metodos de balanceamento
    def __getAltura(self):
        '''
        Se a arvore for vaiza, sua alturae 0.
        Se nao, retorna sua altura
        '''
        if self.__vazia():
            return 0
        else:
            return self.__raiz.__altura
    
    def __setAltura(self, recursao=True):
        '''
        Atualiza a altura da arvore
        '''
        if not(self.__vazia()):
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
    
    def __rotacaoEsquerda(self):
        '''
        Rotaciona uma sub-arvore para a esquerda, pivotando na raiz
        '''
        raiz = self.__raiz
        raiz_direita = self.__raiz.getFilhoDireita().__raiz
        raiz_direita_esquerda = raiz_direita.getFilhoEsquerda().__raiz

        self.__raiz = raiz_direita
        raiz_direita.getFilhoEsquerda().__raiz = raiz
        raiz.getFilhoDireita().__raiz = raiz_direita_esquerda
    
    def __rotacaoDireita(self):
        '''
        Rotaciona uma sub-arvore para a direita, pivotando na raiz
        '''
        raiz = self.__raiz
        raiz_esquerda = self.__raiz.getFilhoEsquerda().__raiz
        raiz_esquerda_direita = raiz_esquerda.getFilhoDireita().__raiz

        self.__raiz = raiz_esquerda
        raiz_esquerda.getFilhoDireita().__raiz = raiz
        raiz.getFilhoEsquerda().__raiz = raiz_esquerda_direita
    
    def __balancear(self):
        '''
        Balanceia uma sub-arvore
        '''
        self.__setAltura(False)
        self.__setBalanceamento(False)
        while abs(self.__balanco) > 1:
            filho_direita = self.__raiz.getFilhoDireita()
            filho_esquerda = self.__raiz.getFilhoEsquerda()
            if self.__balanco > 1:
                if filho_esquerda.__balanco < 0:
                    filho_esquerda.__rotacaoEsquerda() #rotacao dupla (filho esquerda)
                    self.__setAltura()
                    self.__setBalanceamento()
                self.__rotacaoDireita()
            
            if self.__balanco < -1:
                if filho_direita.__balanco > 0:
                    filho_direita.__rotacaoDireita() #rotacao dupla (filho direita)
                    self.__setAltura()
                    self.__setBalanceamento()
                self.__rotacaoEsquerda()
            
            self.__setAltura()
            self.__setBalanceamento()
    
    def __setBalanceamento(self, recursao=True):
        if not(self.__vazia()):
            filho_esquerda = self.__raiz.getFilhoEsquerda()
            filho_direita = self.__raiz.getFilhoDireita()
            if recursao:
                if filho_esquerda is not None:
                    filho_esquerda.__setBalanceamento()
                if filho_direita is not None:
                    filho_direita.__setBalanceamento()
            self.__balanco = filho_esquerda.__altura - filho_direita.__altura
        else:
            self.___balanco = 0
    
    def __getBalanceamento(self):
        '''
        Verifica se a arvore esta balanceada
        '''
        if self is None or self.__vazia():
            return True
        
        filho_esquerda = self.__raiz.getFilhoEsquerda()
        filho_direita = self.__raiz.getFilhoDireita()
        #fazer sempre a verificacao
        self.__setAltura()
        self.__setBalanceamento()

        return (abs(self.__balanco) < 2) and filho_esquerda.__getBalanceamento() and filho_direita.__getBalanceamento()
    #|- --------------------------
    def __sucessor(self,raiz):
        '''
        Encontra o filho mais a esquerda da sub-arvore da direita
        '''
        return super().__sucessor(raiz)
    
    def __antecessor(self, raiz):
        '''
        Encontra filho mais a direita da sub-arvore da esquerda
        '''
        return super().__antecessor(raiz)

    def __procurar(self, chave):
        '''
        Proucura um no na arvore pela sua chave e retorna seu valor ou um erro caso o item nao esteja na arvore
        '''
        return super().__procurar(chave)
    
    def __inserir(self, chave, valor):
        '''
        Insere um novo no na arvore
        '''
        super().__inserir(chave, valor)
        self.__balancear()

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
                        self.__raiz.setChave(substituto.getChave())
                        self.__raiz.setValor(substituto.getValor())
                        self.__raiz.getFilhoDireita().__remover(substituto.getChave())
                self.__balancear()
                return 
            elif chave < self.__raiz.getChave():
                self.__raiz.getFilhoEsquerda().__remover(chave)
            elif chave > self.__raiz.getChave():
                self.__raiz.getFilhoDireita().__remover(chave)
            self.__balancear()
        else:
            raise IndexError('Arvore-Binaria-Busca.__remover(X): x nao esta na arvore')
    #------------------------------
    #Metodos publicos
    def chaves(self):
        '''
        Retorna uma lista com todas as chaves na arvore
        '''
        return super().chaves()

    def valores(self):
        '''
        Retorna uma lista com todos os valores da arvore
        '''
        return super().valores()
    
    def preOrdem(self):
        '''
        Encaminhamento em pre ordem: raiz, filho da esquerda, filho da direita
        '''
        return super().preOrdem()

    def emOrdem(self):
        '''
        Encaminhamento em ordem: filho da esquerda, raiz, filho da direita
        '''
        return super().emOrdem()
    
    def posOrdem(self):
        '''
        Encaminhamento em pos ordem: filho da esquerda, filho da direita, raiz
        '''
        return super().posOrdem()
    #---------------------
    #Metodos magicos
    def __bool__(self):
        '''
        Converte a arvore em valor booleano
        '''
        return super().__bool__()
    
    def __getitem__(self, chave):
        '''
        Retorna o valor contido na chave passada como parametro
        '''
        return super().__getitem__(chave)

    def __setitem__(self, chave, valor):
        '''
        Atualiza o valor de um no se ele estiver na arvore.
        Se nao o insere
        '''
        super().__setitem__(chave, valor)  
    
    def __delitem__(self, chave):
        '''
        Remove um no da arvore com a chave passada como parametro
        '''
        super().__delitem__(chave)

    def __contains__(self, chave):
        '''
        Checa se um item esta na arvore
        '''
        return super().__contains__(chave)

    def __iter__(self):
        '''
        Iterador da arvore
        '''
        return super().__iter__()
    
    def __next__(self):
        '''
        Retorna o no correspondente ao iterador
        '''
        super().__next__()

    def __str__(self):
        '''
        Representacao em str da arvore
        '''
        return super().__str__()
    
    def __repr__(self):
        '''
        Representacao que pode ser instanciada da arvore
        '''
        return super().__repr__()
    #----------------------

def main():
    arvore = ArvoreAVL()

    print('---------------------------------------')
    for i in range(randrange(5, 20)):
        chave = randint(ord('A'), ord('Z'))
        chave = chr(chave)
        if chave not in arvore.chaves():
            print("Inserindo... arvore[{0}] = {1}" .format(chave, i))
        else:
            print("Atualizando... arvore[{0}] de {1} para {2}" .format(chave, arvore[chave], i ))
        arvore[chave] = i
        print("Arvore:", arvore)
        print('---------------------------------------')
    
    for i in range(randrange(1, 10)):
        chave = randint(ord('A'), ord('Z'))
        chave = chr(chave)
        if chave in arvore.chaves():
            print("Removendo... arvore[{0}]" .format(chave))
            del arvore[chave]
            print("Arvore:", arvore)
            print('---------------------------------------')

if __name__ == "__main__":
    main()