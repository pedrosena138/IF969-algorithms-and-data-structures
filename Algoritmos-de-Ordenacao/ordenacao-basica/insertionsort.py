  
"""
Universidade Federal de Pernambuco - UFPE (www.ufpe.br)
Centro de Informática - CIn (www2.cin.ufpe.br) 
Bacharelado em Sistemas de Informação  
Autor: Pedro Manoel Farias Sena de Lima (pmfsl)
Email: pmfsl@cin.ufpe.br
Data: 2019-10-11
Copyright © 2019 todos os direitos reservados
Descricao: Implementacao do algoritmo de ordenacao Insertionsort.
"""
from random import randint
import numpy as np 

def insertionsort(vetor):
    '''
    Divide o vetor entre ordenado na esquerda e desordenado na direita.
    Repete o processo até que todos tenham sido avaliados.
    '''
    tam = len(vetor)
    for i in range(1,tam):
        aux = vetor[i]
        j = i-1
        while (j >= 0) and (vetor[j] > aux):
            vetor[j+1] = vetor[j]
            j -= 1
        vetor[j+1] = aux

def main():
    vetor = np.empty(randint(3,10), int)
    for i in range(len(vetor)):
        elm = randint(0,50)
        while elm in vetor:
            elm = randint(0,50)
        vetor[i] = elm

    print(vetor)
    insertionsort(vetor)
    print(vetor)

if __name__ == "__main__":
    main()

