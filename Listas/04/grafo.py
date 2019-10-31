#-*- coding: utf-8 -*-
"""
Universidade Federal de Pernambuco - UFPE (www.ufpe.br)
Centro de Informática - CIn (www2.cin.ufpe.br) 
Bacharelado em Sistemas de Informação  
Autor: Pedro Manoel Farias Sena de Lima (pmfsl)
Email: pmfsl@cin.ufpe.br
Data: 2019-10-30

Copyright © 2019 todos os direitos reservados

Descricao: Implementacao de um Grafo.
"""
class Grafo:
    def __init__(self, arestas, direcionado=False, ponderado=False):
        self.__arestas = arestas
        self.__grafo = dict()
        self.__direcionado = direcionado
        self.__ponderado = ponderado
        self.__matriz = True
        self.__iniciar()

    def __iniciar(self):
        '''
        Inicia o grafo com as arestas passadas como parametro inicialmente
        '''
        for arestas in self.__arestas:
            if self.__direcionado:
                if self.__ponderado:
                    pass
                else:
                    pass
            else:
                if self.__ponderado:
                    pass
                else:
                    if not(arestas[0] in self.__grafo):
                        self.__grafo[arestas[0]] = [arestas[1]]
                    else:
                        self.__grafo[arestas[0]].append(arestas[1])
                    if not(arestas[1] in self.__grafo):
                        self.__grafo[arestas[1]] = [arestas[0]]
                    else:
                        self.__grafo[arestas[1]].append(arestas[0])

    def inserir_aresta(self, vertice1, vertice2):
        '''
        Insere uma aresta no grafo
        '''
        if self.__direcionado:
            if self.__ponderado:
                pass
            else:
                pass

        else:
            if self.__ponderado:
                pass
            else:
                if not(vertice1 in self.getVertices()) or not(vertice2 in self.getVertices()):
                    raise ValueError("Vertice vertice nao encontrado")
                elif (vertice2 in self.__grafo[vertice1]):
                    raise ValueError("Aresta já existente")
                else:
                    self.__grafo[vertice1].append(vertice2)
                    self.__grafo[vertice2].append(vertice1)
                
    def inserir_vertice(self, vertice):
        '''
        Insere um vertice no grafo
        '''
        if not(vertice in self.__grafo):
            self.__grafo[vertice] = list()
        else:
            raise IndexError("Vertice ja existente")
    
    def remover_aresta(self,vertice1,vertice2):
        '''
        Remove uma aresta do grafo
        '''
        try:
            if self.__ponderado:
                pass
            else:
                if self.__direcionado:
                    self.__grafo[vertice1].remove(vertice2)
                else:
                    self.__grafo[vertice1].remove(vertice2)
                    self.__grafo[vertice2].remove(vertice1)
        except:
            raise IndexError('Vertice nao encontrado')
    
    def remover_vertice(self, vertice):
        '''
        Remove um vertice do grafo
        '''
        try:
            self.__grafo.pop(vertice)
            if self.__ponderado:
                pass
            else:
                for v in self.__grafo:
                    if vertice in self.__grafo[v]:
                        self.__grafo[v].remove(vertice)
        except:
            raise IndexError('Vertice nao encontrado')
            
    def getVertices(self):
        '''
        Retorna os vertices do grafo
        '''
        return list(self.__grafo.keys())
    
    def getArestas(self):
        '''
        Retorna as arestas do grafo
        '''
        lista_arestas = list()
        if self.__direcionado:
            if self.__ponderado:
                pass
            else:
                pass
        else:
            if self.__ponderado:
                pass
            else:
                for vertice1 in self.getVertices():
                    for vertice2 in self.__grafo[vertice1]:
                        if not((vertice1, vertice2,)  in lista_arestas):
                            lista_arestas.append((vertice1, vertice2,))
                            lista_arestas.append((vertice2, vertice1,))
        return lista_arestas

    def ligados(self, vertice1, vertice2):
        '''
        Verifica se dois vertices sao ligados
        '''
        try:
            if self.__ponderado:
                pass
            else:
                if (vertice1, vertice2) in self.getArestas():
                    return True
                else:
                    return False
        except:
            raise IndexError('Vertice nao encontrado')
    
    def adjacentes(self, vertice):
        '''
        Retorna uma lista com os vertices adjacentes ao vertice passado como parametro
        '''
        try:
            if self.__ponderado:
                pass
            else:
                return list(self.__grafo[vertice])
        except:
            raise IndexError('Vertice nao encontrado')   
    
    def grau_entrada(self, vertice):
        '''
        Retorna o grau de entrada do vertice passado como parametro.
        Grau de Entrada: numero de arestas que o vertice e destino
        '''
        try:
            grau = int()
            for arestas in self.getArestas():
                for v in arestas:
                    if v[1] == vertice:
                        grau += 1
            return grau
        except:
            raise IndexError('Vertice nao encontrado')

    def grau_saida(self, vertice):
        '''
        Retorna o grau de saida do vertice passado como parametro.
        Grau de Saida: numero de arestas que o vertice e origem
        '''
        try:
            grau = int()
            for arestas in self.getArestas():
                for v in arestas:
                    if v[0] == vertice:
                        grau += 1
            return grau
        except:
            raise IndexError('Vertice nao encontrado')

    def imprimir_matriz(self):
        '''
        Altera o grafo para matriz de adjacencia
        '''
        if self.__matriz:
            raise ValueError('O grafo já é uma matriz de adjacencia')
        else:
            self.__matriz = True
    
    def imprimir_lista(self):
        '''
        Altera o grafo para lista de adjacencia
        '''
        if self.__matriz:
            self.__matriz = False
        else:
            raise ValueError('O grafo já é uma lista de adjacencia')
    
    def __getitem__(self, vertice):
        '''
        Retorna, em forma de tupla, todas as arestas que se conecta ao vertice passado como parâmetro, se existir peso, retorna com o peso
        '''
        try:
            lista_arestas = list()
            if self.__ponderado:
                pass
            else:
                for v in self.__grafo[vertice]:
                    aresta = (vertice, v)
                    lista_arestas.append(aresta)
            return tuple(lista_arestas)
        except:
            raise IndexError('Vertice nao encontrado')

    def __str__(self):
        '''
        Impressao do grafo
        '''
        if self.__matriz:
            saida = '  '
            for vertice in self.getVertices():
                saida += '  ' + str(vertice)
            saida += '\n'
            for v in self.getVertices():
                saida += str(v) + '  '
                lista_adj = list()
                for u in self.getVertices():
                    if u in self.adjacentes(v):
                        lista_adj.append(1)
                    else:
                        lista_adj.append(0)
                saida += str(lista_adj) + '\n'
        else:
            saida = str()
            for vertice1, vertice2 in self.__grafo.items():
                saida += str(vertice1) + ": " + str(vertice2) + "\n"
        return saida
    
    def __repr__(self):
        '''
        Representação da classe grafo
        '''
        return str(self.__grafo)

def main():
    arestas = ((0,1),(1,2))
    grafo = Grafo(arestas)
    print(grafo)
    
if __name__ == "__main__":
    main()