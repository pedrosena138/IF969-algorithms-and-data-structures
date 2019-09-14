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
Descricao: Implementacao de uma Lista Duplamente Ligada.
'''

from base import ListaDupla

def main():
    lista = ListaDupla('algoritmos')
    print(lista)
    
    lista.Anexar(1)
    print(lista)
    lista.Inserir(1,'O')
    print(lista)
    
    print("\nIndice do 'g' na Lista:",lista.Indice('g'))
    
    lista[0] = 'A'
    print(lista)
    
    print("\nRemover o {} da Lista." .format(lista.Selecionar(1)))
    print(lista)

    lista2 = ListaDupla('lista')
    lista.Concatenar(lista2)
    print('\nA Lista tem {} elemento(s)' .format(len(lista)))
    print(lista)
       
if __name__ == "__main__":
    main()