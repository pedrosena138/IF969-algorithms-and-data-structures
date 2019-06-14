"""
Universidade Federal de Pernanbuco - UFPE (www.ufpe.com.br)
Centro de Informática - CIn (www2.cin.ufpe.br)
Bacharelado em Sistemas de Informação
IF969 - Algoritmos e Estrutura de Dados

Autor: Pedro Manoel Farias Sena de Lima (pmfsl)
Email: pmfsl@cin.ufpe.br
Data: 2019-06-14

Copyright © 2019 todos os direitos reservados
"""

import os
import jogos


def main():
    condicao_jogar = 'S'
    while condicao_jogar == 'S':

        #Escolhendo o modo de jogo
        modo_de_jogo = int(input("Escolha um modo de jogo: \n1-Notakto \n2-Misere \nSua escolha: "))
        while modo_de_jogo != 1 and modo_de_jogo != 2:
            os.system('cls||clear')
            modo_de_jogo = int(input("Escolha um modo de jogo: \n1-Notakto \n2-Misere \nSua escolha: "))

        if  modo_de_jogo == 1:
            os.system('cls||clear')
            jogos.notakto()
        else:
            os.system('cls||clear')
            jogos.misere()

        condicao_jogar = input("\nQuer continuar jogando? [s/n]: ").upper()
        while condicao_jogar != 'S' and condicao_jogar != 'N':
            condicao_jogar = input("Quer continuar jogando? [s/n]: ").upper()

        os.system('cls||clear')

if __name__ == '__main__':
    os.system('cls||clear')
    main()
