import os
import random

H = -1 #Humano
C = +1 #Computador
posicoes = [0,0,0,0,0,0,0,0,0] #posicoes no tabuleiro

def estado_vitoria(posicoes, jogador): 
    """
    Funcao que testa se um determinado jogador venceu a partida
    param posicoes: posicoes atuais no tabuleiro
    param jogador: HUMANO ou COMPUTADOR
    retorna TRUE se o jogador venceu
    """
    vitoria = [
        [posicoes[0], posicoes[1], posicoes[2]],
        [posicoes[3], posicoes[4], posicoes[5]],
        [posicoes[6], posicoes[7], posicoes[8]],
        [posicoes[0], posicoes[3], posicoes[6]],
        [posicoes[1], posicoes[4], posicoes[7]],
        [posicoes[2], posicoes[5], posicoes[8]],
        [posicoes[0], posicoes[4], posicoes[8]],
        [posicoes[2], posicoes[4], posicoes[6]],
    ]

    if [jogador, jogador, jogador] in vitoria:
        return True
    else: 
        return False

def fim_jogo(posicoes):
    """
    Funcao que verifica se o computador ou humano venceu
    param posicoes: posicoes atuais no tabuleiro
    param jogador: HUMANO ou COMPUTADOR
    """
    return estado_vitoria(posicoes, H) or estado_vitoria(posicoes, C)

def celulas_vazias(posicoes):
    """
    Funcao que checa se ainda há células vazias e as adiciona em uma lista
    param posicoes: posicoes atuais no tabuleiro
    retorna uma lista com as celulas vazias
    """
    celulas = []

    c = 0
    while c < len(posicoes):
        if posicoes[c] == 0:
            celulas.append(c)
        c += 1
    return celulas

def movimento_valido(index, posicoes):
    """
    Funcao que verifica se um movimento é valido. Um movimento e valido se a celula e vazia
    param posicoes: posicoes atuais no tabuleiro
    param index: indice da celula vazia
    retorna TRUE se posicoes[index] for vazia
    """
    if index in celulas_vazias(posicoes):
        return True
    else:
        return False

def set_move(index, jogador):
    """
    Funcao que faz a jogada no tabuleiro
    param index: indice no tabuleiro
    param jogador: jogador que esta fazendo a jogada
    param posicoes: posicoes atuais no tabuleiro
    """
    if movimento_valido(index, posicoes):
        posicoes[index] = jogador
        return True
    else:
        return False 

def tabuleiro(posicoes, modo_normal):
    """
    Funcao para imprimir o tabuleiro de jogo
    param posicoes: condicao atual do tabuleiro
    param modo_normal: define se o jogo vai ser jogado com 'X e O' ou so 'X'
    """
    divisor = '\t-----------------------'
    #caso exista X e O no jogo
    if modo_normal:
        for x in range(len(posicoes)):
            if x%3 == 0:
                print("\n" + divisor)

            if posicoes[x] == -1:
                print(f'\t|  X  |', end='')
            elif posicoes[x] == +1:
                print(f'\t|  O  |', end='')
            else:
                print(f'\t|     |', end='')
        print("\n" + divisor)
    #caso exista so X no jogo
    else:
        for x in range(len(posicoes)):
            if x%3 == 0:
                print("\n" + divisor)
            
            if posicoes[x] == 1:
                print(f'\t|  X  |', end='')
            else:
                print(f'\t|     |', end='')
        print("\n" + divisor) 

def notakto(modo_normal = False):
    while len(celulas_vazias(posicoes)) > 0 and not fim_jogo(posicoes):
        os.system('cls||clear')
        print("========================================")
        print("                NOTAKTO                 ")
        print("========================================")
    
        tabuleiro(posicoes, modo_normal)
    """
        jogada_h = int(input("Escolha uma casa [1 a 9]: "))
        
        while not(movimento_valido(posicoes, (jogada_h))):
            try:
                jogada_h = int(input("Jogada invalida. Escolha uma casa [1 a 9]: "))
            except (KeyError, ValueError):
                print('')
        posicoes[jogada_h-1] = 1
    tabuleiro(posicoes, modo_normal)

        tabuleiro(posicoes, modo_normal)

        jogada_c = random.randint(0,9)
        while movimento_valido(posicoes, (jogada_c-1)):
            try:
                jogada_c = random.randint(0,9)
            except (KeyError, ValueError):
                print('')

        posicoes[jogada_c] = -1
        tabuleiro(posicoes, modo_normal)
    """

def misere(modo_normal):
    while len(celulas_vazias(posicoes)) > 0 and not fim_jogo(posicoes):
        os.system('cls||clear')
        print("========================================")
        print("                MISERE                  ")
        print("========================================")
    
        tabuleiro(posicoes, modo_normal)
"""
        jogada_h = int(input("\nEscolha uma casa [1 a 9]: "))
        while movimento_valido(posicoes, (jogada_h-1)):
            try:
                jogada_h = int(input("\nEscolha uma casa [1 a 9]: "))
            except (KeyError, ValueError):
                print('')

        posicoes[jogada_h-1] = 1

        tabuleiro(posicoes, modo_normal)

        jogada_c = random.randint(0,9)
        while movimento_valido(posicoes, (jogada_c-1)):
            try:
                jogada_c = random.randint(0,9)
            except (KeyError, ValueError):
                print('')

        posicoes[jogada_c] = -1
"""