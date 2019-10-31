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
            if self.__ponderado:
                try:
                    if self.__direcionado:
                        pass
                    else:
                        if not(arestas[0] in self.__grafo):
                            self.__grafo[arestas[0]] = [(arestas[1],arestas[2],)]
                        else:
                            self.__grafo[arestas[0]].append((arestas[1],arestas[2],))
                        if not(arestas[1] in self.__grafo):
                            self.__grafo[arestas[1]] = [(arestas[0],arestas[2],)]
                        else:
                            self.__grafo[arestas[1]].append((arestas[0],arestas[2],))
                except:
                    raise ValueError("Aresta sem peso")
            else:
                if self.__direcionado:
                    if not(arestas[0] in self.__grafo):
                        self.__grafo[arestas[0]] = [arestas[1]]
                    else:
                        self.__grafo[arestas[0]].append(arestas[1])
                    if not(arestas[1] in self.__grafo):
                        self.__grafo[arestas[1]] = list()
                else:
                    if not(arestas[0] in self.__grafo):
                        self.__grafo[arestas[0]] = [arestas[1]]
                    else:
                        self.__grafo[arestas[0]].append(arestas[1])
                    if not(arestas[1] in self.__grafo):
                        self.__grafo[arestas[1]] = [arestas[0]]
                    else:
                        self.__grafo[arestas[1]].append(arestas[0])

    def inserir_aresta(self, vertice1, vertice2,peso=0):
        '''
        Insere uma aresta no grafo
        '''
        if self.__ponderado:
            if (vertice1 in self.getVertices()) and (vertice2 in self.getVertices()):
                if peso == 0:
                    raise ValueError("Aresta sem peso")
                else:
                    if self.__direcionado:
                        self.__grafo[vertice1].append((vertice2,peso))
                        self.__grafo[vertice1].sort()
                    else:
                        self.__grafo[vertice1].append((vertice2,peso))
                        self.__grafo[vertice2].append((vertice1,peso))
                        self.__grafo[vertice1].sort()
                        self.__grafo[vertice2].sort()
            else:
                raise IndexError("Vertice nao encontrado")
        else:
            if (vertice1 in self.getVertices()) and (vertice2 in self.getVertices()):
                if self.__direcionado:
                    if vertice2 in self.__grafo[vertice1]:
                        raise ValueError("Aresta já existente")
                    else:
                        self.__grafo[vertice1].append(vertice2)
                        self.__grafo[vertice1].sort()
                else:
                    if vertice2 in self.__grafo[vertice1] or vertice1 in self.__grafo[vertice2]:
                        raise ValueError("Aresta já existente")
                    else:
                        self.__grafo[vertice1].append(vertice2)
                        self.__grafo[vertice2].append(vertice1)
                        self.__grafo[vertice1].sort()
                        self.__grafo[vertice2].sort()
            else:
                raise IndexError("Vertice nao encontrado")
                
    def inserir_vertice(self, vertice):
        '''
        Insere um vertice no grafo
        '''
        if not(vertice in self.__grafo):
            self.__grafo[vertice] = list()
        else:
            raise IndexError("Vertice ja existente")
    
    def remover_aresta(self,vertice1,vertice2,peso=0):
        '''
        Remove uma aresta do grafo
        '''
        if (vertice1 in self.getVertices()) and (vertice2 in self.getVertices()):
            if self.__ponderado:
                if peso == 0:
                    raise ValueError("Aresta sem peso")
                else:
                    if (vertice2,peso) in self.__grafo[vertice1]:
                        self.__grafo[vertice1].remove((vertice2,peso))
                        if not(self.__direcionado):
                            self.__grafo[vertice2].remove((vertice1,peso))
                    else:
                        raise ValueError("Aresta nao encontrada")
            else:
                self.__grafo[vertice1].remove(vertice2)
                if not(self.__direcionado):
                    self.__grafo[vertice2].remove(vertice1)
        else:
            raise IndexError('Aresta nao encontrada')
    
    def remover_vertice(self, vertice):
        '''
        Remove um vertice do grafo
        '''
        try:
            self.__grafo.pop(vertice)
            for v in self.__grafo:
                if self.__ponderado:
                    for adjacente in self.__grafo[v]:
                        if adjacente[0] == vertice:
                            self.__grafo[v].remove(adjacente)
                else:
                    if vertice in self.__grafo[v]:
                        self.__grafo[v].remove(vertice)         
        except:
            raise IndexError('Vertice nao encontrado')
            
    def getVertices(self):
        '''
        Retorna os vertices do grafo
        '''
        lista_vertices = list(self.__grafo.keys())
        lista_vertices.sort()
        return lista_vertices
    
    def getArestas(self):
        '''
        Retorna as arestas do grafo
        '''
        lista_arestas = list()
        for vertice in self.getVertices():
            for adjacente in self.__grafo[vertice]:
                if self.__ponderado:
                    if not((vertice, adjacente[0], adjacente[1])  in lista_arestas):
                        lista_arestas.append((vertice, adjacente[0], adjacente[1]))
                else:
                    if not((vertice, adjacente)  in lista_arestas):
                        lista_arestas.append((vertice, adjacente))
        lista_arestas.sort()
        return lista_arestas

    def ligados(self, vertice1, vertice2):
        '''
        Verifica se dois vertices sao ligados
        '''
        try:
            if self.__ponderado:
                encontrado = False
                for vertice in self.__grafo[vertice1]:
                    if vertice2 == vertice[0]:
                        encontrado = True
                return encontrado
            else:
                if vertice2 in self.__grafo[vertice1]:
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
                lista_adj = list()
                for adjacente in self.__grafo[vertice]:
                    if not(adjacente[0] in lista_adj):
                        lista_adj.append(adjacente[0])
                lista_adj.sort()
                return lista_adj
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
            if vertice in self.getVertices():
                grau = int()
                for aresta in self.getArestas():
                    if aresta[1] == vertice:
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
            if vertice in self.getVertices():
                grau = int()
                for aresta in self.getArestas():
                    if aresta[0] == vertice:
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
            for v in self.__grafo[vertice]:
                if self.__ponderado:
                    aresta = (vertice, v[0], v[1])
                else:
                    aresta = (vertice, v)
                lista_arestas.append(aresta)
            lista_arestas.sort()
            return tuple(lista_arestas)
        except:
            raise IndexError('Vertice nao encontrado')

    def __str__(self):
        '''
        Impressao do grafo
        '''
        saida = str()
        if self.__matriz:
            saida = '  '
            for vertice in self.getVertices():
                saida += '  ' + str(vertice)
            saida += '\n'
            for v in self.getVertices():
                saida += str(v) + '  '
                lista_adj = list()
                if self.__ponderado:  arestas = self.__getitem__(v)
                for u in self.getVertices():
                    if self.__ponderado:
                        valor = int()
                        ocorrencia = int()
                        for i in range(len(arestas)):
                            if u == arestas[i][1]:
                                valor += arestas[i][2]
                                ocorrencia += 1
                        if ocorrencia > 1: #caso haja arestas para o mesmo destino, o grafo ira contabilizar a divisao exata dos pesos pela quantidade de ocorrencias
                            valor //= ocorrencia
                        lista_adj.append(valor)
                    else:
                        if u in self.adjacentes(v):
                            lista_adj.append(1)
                        else:
                            lista_adj.append(0)
                saida += str(lista_adj) + '\n'
        else:
            for vertice, adjacentes in self.__grafo.items():
                saida += str(vertice) + ": " + str(adjacentes) + "\n"
        return saida
    
    def __repr__(self):
        '''
        Representação da classe grafo
        '''
        return str(self.__grafo)

def grafo1():
    arestas = ((0,1),(1,2), (2,3), (3,1))
    grafo = Grafo(arestas)
    print(grafo)

    grafo.inserir_vertice(4)
    grafo.inserir_aresta(4,0)
    print(grafo)

    grafo.remover_aresta(1,3)
    grafo.remover_vertice(4)
    print(grafo)

    print(grafo.ligados(0,1))
    print(grafo.adjacentes(2))
    print(grafo.grau_entrada(1))
    print(grafo.grau_saida(2))
    grafo.imprimir_matriz()
    print(grafo)

def grafo2():
    arestas = ((0,1), (0,2), (1,2), (2,3))
    grafo = Grafo(arestas, True)
    print(grafo)

def grafo3():
    arestas = ((0,1,4),(1,2,7), (2,3,2), (3,1,2))
    grafo = Grafo(arestas, False, True)
    print(grafo)

def main():
    grafo3()
    
if __name__ == "__main__":
    main()