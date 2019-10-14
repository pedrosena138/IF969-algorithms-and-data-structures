  
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

def selectionsort(vetor):
    '''
    Checa todo o vetor primeiro para pegar o menor elemento, depois realiza a troca
    '''
    tam = len(vetor)
    for i in range(0,tam):
        min = i
        for j in range(i+1,tam):
            if vetor[min] > vetor[j]:
                min = j
        trocar(vetor, i, min)

def main():
    vetor = np.empty(randint(3,10), int)
    for i in range(len(vetor)):
        elm = randint(0,50)
        while elm in vetor:
            elm = randint(0,50)
        vetor[i] = elm

    print(vetor)
    selectionsort(vetor)
    print(vetor)

if __name__ == "__main__":
    main()

