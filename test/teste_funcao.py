"""
Arquivo que contem as configuracoes dos jogos Notaktoe e Misere
"""
import os
import random

#var globais
H = -1 #Humano
C = +1 #Computador

def estado_vitoria(posicoes, jogador): 
    """
    Funcao que testa se um determinado jogador venceu a partida
    param posicoes: posicoes atuais no tabuleiro
    param jogador: HUMANO ou COMPUTADOR
    param modo normal: verifica se o modo de jogo e o Notaktoe ou o Misere
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

def tabuleiro(posicoes, tabuleiro_normal):
    """
    Funcao para imprimir o tabuleiro de jogo
    param posicoes: condicao atual do tabuleiro
    param modo_normal: define se o jogo vai ser jogado com 'X e O' ou so 'X'
    """
    divisor = '\t-----------------------'
    #caso exista X e O no jogo
    if tabuleiro_normal:
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

def setMove(jogador, posicoes, index):
    """
    Funcao que faz a jogada no tabuleiro
    param index: indice no tabuleiro
    param jogador: jogador que esta fazendo a jogada
    param posicoes: posicoes atuais no tabuleiro
    param index: verifica se e a ia que esta jogando
    """
    if jogador == 1:
        while not (movimento_valido(jogador-1, posicoes) or fim_jogo(posicoes)):
            try:
                jogador = int(input("Escolha uma casa [1 a 9]: "))
            except (KeyError, ValueError):
                print('Insira um valor válido. ', end='')
            
    else:
        if len(celulas_vazias(posicoes)) > 0:
            jogador = random.choice(celulas_vazias(posicoes))
        
    return jogador

def msg_final(posicoes, modo_normal, tabuleiro_normal):
    tabuleiro(posicoes, tabuleiro_normal)
    if modo_normal:
        if estado_vitoria(posicoes, H):
            print("\nVITORIA!!!")
        elif estado_vitoria(posicoes, C):
            print("\nDERROTA :(")
        else:
            print("\nEMPATE...")
    else:
        if estado_vitoria(posicoes, H):
            print("\nDERROTA :(")
        elif estado_vitoria(posicoes, C):
            print("\nVITORIA!!!")
        else:
            print("\nEMPATE...")

def notakto(modo_normal):
    posicoes = [0,0,0,0,0,0,0,0,0] #posicoes no tabuleiro
    jogada_h = int() #jogada do humano
    jogada_c = int() #jogada do computador

    while len(celulas_vazias(posicoes)) > 0 and not fim_jogo(posicoes):
        os.system('cls||clear')
        print("========================================")
        print("                NOTAKTO                 ")
        print("========================================")

        tabuleiro(posicoes, False)
        print('')

        jogada_h = setMove(H,posicoes,jogada_h)
        posicoes[jogada_h-1] = 1
        
        jogada_c = setMove(C,posicoes,jogada_c)
        posicoes[jogada_c-1] = 1
    
    os.system('cls||clear')
    print("========================================")
    print("                NOTAKTOE                  ")
    print("========================================")
    msg_final(posicoes, modo_normal, False)