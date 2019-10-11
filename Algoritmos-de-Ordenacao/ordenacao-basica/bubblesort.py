  
"""
Universidade Federal de Pernambuco - UFPE (www.ufpe.br)
Centro de Informática - CIn (www2.cin.ufpe.br) 
Bacharelado em Sistemas de Informação  
Autor: Pedro Manoel Farias Sena de Lima (pmfsl)
Email: pmfsl@cin.ufpe.br
Data: 2019-10-11
Copyright © 2019 todos os direitos reservados
Descricao: Implementacao do algoritmo de ordenacao Bubblesort.
"""
from random import randint

def bubblesort(vetor):
    '''
    Troca o elemento consecutivamente de lugar caso ele seja maior que o próximo
    '''
    tam = len(vetor)
    for i in range(0,tam-1)   :
        for j in range(i+1,tam):
            if vetor[i] > vetor[j]:
                aux = vetor[i]
                vetor[i] = vetor[j]
                vetor[j] = aux