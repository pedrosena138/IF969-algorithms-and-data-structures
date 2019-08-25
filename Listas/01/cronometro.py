"""
Universidade Federal de Pernanbuco - UFPE (www.ufpe.br)
Centro de Informática - CIn (www2.cin.ufpe.br)
Bacharelado em Sistemas de Informação
IF969 - Algoritmos e Estrutura de Dados

Autor: Pedro Manoel Farias Sena de Lima (pmfsl)
Email: pmfsl@cin.ufpe.br
Data: 2019-08-25
 
Copyright © 2019 todos os direitos reservados

Descrição: Q1.Criar um cronômetro;
           Q2.Implementar os métodos '__str__' e __repr__;
           Q3. Adicionar getters e deixar os atributos privados.
"""
from time import perf_counter

class Cronometro:
    def __init__(self):
        self.__tempoInicio = float()
        self.__tempoFim = float()
        self.__tempoTotal = float()
        self.__tempoParado = True
    
    def __getTempoInicio(self):
        return self.__tempoInicio
    def __setTempoInicio(self, tempo):
        self.__tempoInicio = tempo
    
    def __getTempoFim(self):
        return self.__tempoFim
    def __setTempoFim(self, tempo):
        self.__tempoFim = tempo
    
    def __getTempoTotal(self):
        return self.__tempoTotal
    def __setTempoTotal(self, tempoFinal, tempoInicial):
        self.__tempoTotal = tempoFinal - tempoInicial

    def __getTempoParado(self):
        return self.__tempoParado
    def __setTempoParado(self, estado):
        self.__tempoParado = estado

    def Iniciar(self):
        tempo = perf_counter()
        self.__setTempoInicio(tempo) 
        self.__setTempoParado(False)

    def Parar(self):
        tempo = perf_counter()
        self.__setTempoFim(tempo) 
        self.__setTempoParado(True)

    def Zerar(self):
        self.__setTempoInicio(0.0)
        self.__setTempoFim(0.0)
    
    def __exibir(self):
        if self.__getTempoParado():
            tempoFinal = self.__getTempoFim()
            tempoInicial = self.__getTempoInicio()
            self.__setTempoTotal(tempoFinal, tempoInicial)

            return self.__getTempoTotal()
        else:
            tempoAtual = perf_counter()
            tempoInicial = self.__getTempoInicio()
            self.__setTempoTotal(tempoAtual, tempoInicial)
            
            return self.__getTempoTotal()
    
    def __repr__(self):
        return float("%f " % self.__exibir())

    def __str__(self):
        return ("%f seg" % self.__exibir())

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