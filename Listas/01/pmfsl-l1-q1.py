"""
Universidade Federal de Pernanbuco - UFPE (www.ufpe.com.br)
Centro de Informática - CIn (www2.cin.ufpe.br)
Bacharelado em Sistemas de Informação
IF969 - Algoritmos e Estrutura de Dados

Autor: Pedro Manoel Farias Sena de Lima (pmfsl)
Email: pmfsl@cin.ufpe.br
Data: 2019-08-23

Copyright © 2019 todos os direitos reservados

Descrição: Escreva em Python uma classe Cronometro, que seja capaz de cronometrar o tempo passado no sistema 
a partir de dois métodos (iniciar e parar). Para isso você pode importar a biblioteca time e usar o método 
time.clock() para obter o tempo atual do sistema. A classe Cronometro deve implementar os seguintes métodos:

Construtor - Método construtor padrão de qualquer objeto
Iniciar - Inicia a contagem do tempo do relógio
Parar - Para a contagem do tempo do relógio
Zerar - Zera o contador
Exibir - Exibe o tempo contado pelo cronômetro
"""
import time
class Cronometro:
    #def __init__(self)
    pass

parar_tempo = False

tempo = float()
while not(parar_tempo):
    tempo += time.clock()
    print(tempo)
