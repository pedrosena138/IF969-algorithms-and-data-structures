  
"""
Universidade Federal de Pernambuco - UFPE (www.ufpe.br)
Centro de Informática - CIn (www2.cin.ufpe.br) 
Bacharelado em Sistemas de Informação  
Autor: Pedro Manoel Farias Sena de Lima (pmfsl)
Email: pmfsl@cin.ufpe.br
Data: 2019-10-11
Copyright © 2019 todos os direitos reservados
Descricao: Implementacao do algoritmo de ordenacao Selectionsort.
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

def shellsort(vetor):
    '''
    Funciona similar ao Insertionsort, porém possui  mais pivôs de comparação (h). Como foi mostrado por Knuth:
    h(1) = 1
    H(s) = 3*h(s-1) + 1
    '''
    tam = len(vetor)
    h = 1

    while h < tam//3:
        h = 3*h + 1
    
    while h >= 1:
        for i in range(h, tam):
            j = i
            while (j >= h) and (vetor[j] < vetor[j-h]):
                trocar(vetor, j, j-h)
                j -= h
        h //= 3

def main():
    vetor = np.empty(50, int)
    for i in range(len(vetor)):
        elm = randint(0,50)
        while elm in vetor:
            elm = randint(0,50)
        vetor[i] = elm

    print(vetor)
    shellsort(vetor)
    print(vetor)

if __name__ == "__main__":
    main()

