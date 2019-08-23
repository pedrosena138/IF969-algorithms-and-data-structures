"""
Universidade Federal de Pernanbuco - UFPE (www.ufpe.br)
Centro de Informática - CIn (www2.cin.ufpe.br)
Bacharelado em Sistemas de Informação
IF969 - Algoritmos e Estrutura de Dados

Autor: Pedro Manoel Farias Sena de Lima (pmfsl)
Email: pmfsl@cin.ufpe.br
Data: 2019-08-23
 
Copyright © 2019 todos os direitos reservados

Descrição: Criar um cronômetro
"""
from time import perf_counter

class Cronometro:
    def __init__(self):
        self.__tempo = float()
        self.__contarTempo = None
    
    def Iniciar(self):
        self.__tempo = perf_counter()
    #Nao funciona
    def Parar(self):
        self.__contarTempo = False

    #Nao funciona 
    def Zerar(self):
        pass
    
    def Exibir(self):
        return self.__tempo

def main():
    cronometro = Cronometro()
    cronometro.Iniciar()
    print(cronometro.Exibir())
    print(cronometro.Exibir())
    print(cronometro.Exibir())
    print(cronometro.Exibir())

if __name__ == "__main__":
    main()