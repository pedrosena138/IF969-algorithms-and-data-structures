  
"""
Universidade Federal de Pernambuco - UFPE (www.ufpe.br)
Centro de Informática - CIn (www2.cin.ufpe.br) 
Bacharelado em Sistemas de Informação  
Autor: Pedro Manoel Farias Sena de Lima (pmfsl)
Email: pmfsl@cin.ufpe.br
Data: 2019-10-11
Copyright © 2019 todos os direitos reservados
Descricao: Implementacao do algoritmo de ordenacao Quicksort.
"""
from random import randint
import numpy as np 

def trocar(vetor, i, j):
    '''
    Troca as posicoes do vetor
    '''
    aux = vetor[i]
    vetor[i] = vetor[j]
    vetor[j] = aux

def particao(vetor, esquerda, direita):
    '''
    Particiona o vetor
    '''
    pivo = vetor[esquerda]
    i = esquerda
    j = direita + 1
    while True:
        i += 1
        while vetor[i] < pivo:
            if i >= direita:
                break
            i += 1
        j -= 1
        while vetor[j] > pivo:
            if j <= esquerda:
                break
            j -= 1
        if i >= j:
            break
        trocar(vetor, i, j)
    trocar(vetor, esquerda, j)
    return j

def recursao_qs(vetor, esquerda, direita):
    '''
    Chama o quicksort recursivamente
    '''
    if esquerda >= direita:
        return
    p = particao(vetor, esquerda, direita)
    recursao_qs(vetor, esquerda, p-1)
    recursao_qs(vetor, p+1, direita)

def quicksort(vetor):
    '''
    Metodo principal do quicksort
    '''
    tam = len(vetor)
    recursao_qs(vetor, 0, tam-1)
    
def main():
    vetor = np.empty(randint(3,10), int)
    for i in range(len(vetor)):
        elm = randint(0,50)
        while elm in vetor:
            elm = randint(0,50)
        vetor[i] = elm

    print(vetor)
    quicksort(vetor)
    print(vetor)

if __name__ == "__main__":
    main()

