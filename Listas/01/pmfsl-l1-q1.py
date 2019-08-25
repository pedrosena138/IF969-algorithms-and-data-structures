"""
Universidade Federal de Pernanbuco - UFPE (www.ufpe.br)
Centro de Informática - CIn (www2.cin.ufpe.br)
Bacharelado em Sistemas de Informação
IF969 - Algoritmos e Estrutura de Dados

Autor: Pedro Manoel Farias Sena de Lima (pmfsl)
Email: pmfsl@cin.ufpe.br
Data: 2019-08-25
 
Copyright © 2019 todos os direitos reservados

Descrição: Criar um cronômetro
"""
from time import perf_counter

class Cronometro:
    def __init__(self):
        self.__tempoInicio = float()
        self.__tempoFim = float()
        self.__tempoTotal = float()
        self.__tempoParado = None
    
    def Iniciar(self):
        self.__tempoInicio = perf_counter()
        self.__tempoParado = False

    def Parar(self):
        self.__tempoFim = perf_counter()
        self.__tempoParado = True

    def Zerar(self):
        self.__tempoInicio = 0.0
        self.__tempoFim = 0.0
    
    def Exibir(self):
        if self.__tempoParado:
            self.__tempoTotal = self.__tempoFim - self.__tempoInicio
            return self.__tempoTotal
        else:
            self.__tempoTotal = perf_counter() - self.__tempoInicio
            return self.__tempoTotal

def main():
    cronometro = Cronometro()
    cronometro.Iniciar()
    print("%f seg" % cronometro.Exibir())
    print("%f seg" % cronometro.Exibir())
    print("%f seg" % cronometro.Exibir())
    print("")
    cronometro.Parar()
    print("%f seg" % cronometro.Exibir())
    print("%f seg" % cronometro.Exibir())
    print("%f seg" % cronometro.Exibir())
    print("")
    cronometro.Zerar()
    print("%f seg" % cronometro.Exibir())
    print(" ")
    cronometro.Iniciar()
    print("%f seg" % cronometro.Exibir())
    print("%f seg" % cronometro.Exibir())
    print("%f seg" % cronometro.Exibir())


if __name__ == "__main__":
    main()