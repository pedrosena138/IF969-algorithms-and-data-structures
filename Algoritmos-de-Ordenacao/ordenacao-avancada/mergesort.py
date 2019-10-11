  
"""
Universidade Federal de Pernambuco - UFPE (www.ufpe.br)
Centro de Informática - CIn (www2.cin.ufpe.br) 
Bacharelado em Sistemas de Informação  
Autor: Pedro Manoel Farias Sena de Lima (pmfsl)
Email: pmfsl@cin.ufpe.br
Data: 2019-10-11
Copyright © 2019 todos os direitos reservados
Descricao: Implementacao do algoritmo de ordenacao Mergesort.
"""
from random import randint
import numpy as np 

def merge(vetor, esquerda, meio, direita):
    i = esquerda
    j = meio + 1
    for k in range(esquerda, direita+1):
        aux[k] = vetor[k]
        if i > meio:
            vetor[k] = aux[j]
            j += 1
        elif j > direita:
            vetor[k] = aux[i]
            i += 1
        elif aux[i] > aux[j]:
            vetor[k] = aux[j]
            j += 1
        else:
            vetor[k] = aux[i]
            i += 1

#Mergesort Top-Down
def TD_mergesort(vetor, esquerda, direita):
    if esquerda >= direita:
        return
    meio = (esquerda + direita)//2
    TD_mergesort(vetor, esquerda, meio)
    TD_mergesort(vetor, meio+1, direita)
    merge(vetor, esquerda, meio, direita)

#Mergesort Bottom-Up
def BU_mergesort(vetor):
    tam = len(vetor)
    global aux
    aux = list(vetor)
    k = 1
    while k < tam:
        for esquerda in range(0, tam-k, 2*k):
            merge(vetor, esquerda, esquerda+k-1, min(esquerda+(2*k)-1, tam-1))
        k *= 2
    del aux

def mergesort(vetor):
    tam = len(vetor)
    global aux
    aux = list(vetor)
    TD_mergesort(vetor, 0, tam-1)
    del aux
    
def main():
    vetor = np.empty(randint(3,10), int)
    for i in range(len(vetor)):
        elm = randint(0,50)
        while elm in vetor:
            elm = randint(0,50)
        vetor[i] = elm

    print(vetor)
    mergesort(vetor)
    print(vetor)

if __name__ == "__main__":
    main()

