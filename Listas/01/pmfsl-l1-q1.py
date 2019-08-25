"""
Universidade Federal de Pernanbuco - UFPE (www.ufpe.br)
Centro de Informática - CIn (www2.cin.ufpe.br)
Bacharelado em Sistemas de Informação
IF969 - Algoritmos e Estrutura de Dados

Autor: Pedro Manoel Farias Sena de Lima (pmfsl)
Email: pmfsl@cin.ufpe.br
Data: 2019-08-25
 
Copyright © 2019 todos os direitos reservados

Descrição: Q1.Criar um cronômetro
           Q2.Implementar os métodos '__str__' e __repr__
"""
from time import perf_counter

class Cronometro:
    def __init__(self):
        self.__tempoInicio = float()
        self.__tempoFim = float()
        self.__tempoTotal = float()
        self.__tempoParado = True
    
    def Iniciar(self):
        self.__tempoInicio = perf_counter()
        self.__tempoParado = False

    def Parar(self):
        self.__tempoFim = perf_counter()
        self.__tempoParado = True

    def Zerar(self):
        self.__tempoInicio = 0.0
        self.__tempoFim = 0.0
    
    def __Exibir(self):
        if self.__tempoParado:
            self.__tempoTotal = self.__tempoFim - self.__tempoInicio
            return self.__tempoTotal
        else:
            self.__tempoTotal = perf_counter() - self.__tempoInicio
            return self.__tempoTotal
    
    # Questao 02
    def __repr__(self):
        return float("%f " % self.__Exibir())

    def __str__(self):
        return ("%f seg" % self.__Exibir())

def main():
    cronometro = Cronometro()

    cronometro.Iniciar()
    print(cronometro)
    print(cronometro)
    print(cronometro)
    print("")

    cronometro.Parar()
    print(cronometro)
    print(cronometro)
    print(cronometro)
    print("")

    cronometro.Zerar()
    print(cronometro)
    print(" ")
    
    cronometro.Iniciar()
    print(cronometro)
    print(cronometro)
    print(cronometro)


if __name__ == "__main__":
    main()