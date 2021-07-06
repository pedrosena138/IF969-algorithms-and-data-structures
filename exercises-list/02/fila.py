'''
Universidade Federal de Pernambuco - UFPE (www.ufpe.br)
Centro de Informática - CIn (www2.cin.ufpe.br) 
Bacharelado em Sistemas de Informação 
IF969 - Algoritmos e Estrutura de Dados 
Professor: Hansenclever Bassani 
Autor: Pedro Manoel Farias Sena de Lima (pmfsl)
Email: pmfsl@cin.ufpe.br
Data: 2019-09-14
Copyright © 2019 todos os direitos reservados
Descricao: Implementacao de uma Fila.
'''

from base import Fila

def main():
    fila = Fila('algoritmos')
    print(fila)

    fila.Enqueue('O')
    print(fila)

    print("\nIndice do 's' na Fila:",fila.Indice('s'))
    fila[9] = 'S'
    print(fila)

    fila.Dequeue()
    print(fila)

    fila2 = Fila('fila')
    fila.Concatenar(fila2)
    print('\nA Fila tem {} elemento(s)' .format(len(fila)))
    print(fila)
    
if __name__ == "__main__":
    main()
