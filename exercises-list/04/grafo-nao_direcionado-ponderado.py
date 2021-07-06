#-*- coding: utf-8 -*-

from grafo import Grafo 

def main():
    '''
    Grafo nao-direcionado ponderado
    '''
    arestas = ((0,1,4),(1,2,7), (2,3,2), (3,1,2))
    grafo = Grafo(arestas, False, True)
    print(grafo)
    
    print("Os vertices (0) e (1) sao ligados?", grafo.ligados(0,1))
    print("Vertices adjacentes ao vertice (1):", grafo.adjacentes(1))
    print("Grau de entrada do vertice (2):", grafo.grau_entrada(2))
    print("Grau de saida do vertice (3):",grafo.grau_saida(3))

    print("Insercao do vertice (4)")
    grafo.inserir_vertice(4)
    print(grafo)
    
    print("Insercao da aresta (4,0,7)")
    grafo.inserir_aresta(4,0,7)
    print(grafo)

    print("Remoção da aresta (1,3,2)")
    grafo.remover_aresta(1,3,2)
    print(grafo)

    print("Remoção do vertice (2)")
    grafo.remover_vertice(2)
    print(grafo)

    print("Matriz de Adjacencia")
    grafo.imprimir_matriz()
    print(grafo)
if __name__ == "__main__":
    main()