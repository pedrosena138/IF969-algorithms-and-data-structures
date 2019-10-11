  
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
        aux = vetor[i]
        vetor[i] = vetor[min]
        vetor[min] = aux

lista = list()
for i in range(randint(3,13)):
    elm = randint(0,50)
    while elm in lista:
        elm = randint(0,50)
    lista.append(elm)
print(lista)

selectionsort(lista)
print(lista)

