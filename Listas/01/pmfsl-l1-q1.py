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
from time import clock
class Cronometro:
    def __init__(self):
        self.__tempo = float()
        self.__contarTempo = None
    
    def Iniciar(self):
        self.__contarTempo = True
        while self.__contarTempo:
            self.__tempo = clock()

    def Parar(self):
        self.__contarTempo = False

    def Zerar(self):
        self.__tempo = 0.0
    
    def Exibir(self):
        return self.__tempo

if __name__ == "__main__":
    cronometro = Cronometro()
    cronometro.Iniciar()
    cronometro.Parar()
    print(cronometro.Exibir())

    cronometro.Iniciar()
    n = input("Digite algo: ")
    cronometro.Parar()
    print(cronometro.Exibir())

    cronometro.Zerar()
    cronometro.Iniciar()
    cronometro.Parar()
    print(cronometro.Exibir())
 