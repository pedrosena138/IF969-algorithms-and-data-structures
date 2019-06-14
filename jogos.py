import os
import random
escolha_h = int() #escolha do humano
escolha_c = int() #escolha do computador

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
            elif posicoes[x] == 1:
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

def celula_vazia(posicoes, index):
    """
    Funcao que checa se ainda há movimentos válidos
    """
    if posicoes[index] == 0:
        return True
    else:
        return False

def movimento_valido(posicoes, index):
    if index >= 0 and index <= 8 and celula_vazia(posicoes, index) : 
        return True
    else:
        return False

def game_over(posicoes):
    if 0 in posicoes:
        return False
    else:
        return True

def notakto(modo_normal, posicoes = [0,0,0,0,0,0,0,0,0]):
    while not(game_over(posicoes)):
        os.system('cls||clear')
        print("========================================")
        print("                NOTAKTO                 ")
        print("========================================")
    
        tabuleiro(posicoes, modo_normal)

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
        tabuleiro(posicoes, modo_normal)

        
def misere(modo_normal, posicoes = [0,0,0,0,0,0,0,0,0]):
    while game_over(posicoes):
        os.system('cls||clear')
        print("========================================")
        print("                MISERE                  ")
        print("========================================")
    
        tabuleiro(posicoes, modo_normal)

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
    escolha_j = str()  # escolha do jogador
    escolha_c = str()  # escolha do computador
    primeiro_jogar = str()  # primeiro a jogar (jogador ou computador)

    # Setando o jogador
    while escolha_j != 'X' and escolha_j != 'O':
        os.system('cls||clear')
        escolha_j = input("Escolha - X ou O: ").upper()

    #Setando o computador
    if escolha_j == 'X':
        escolha_c = 'O'
    else:
        escolha_c = 'X'

    os.system('cls||clear')
    #Setando o inicio de jogo
    while primeiro_jogar != 'S' and primeiro_jogar != 'N':
        os.system('cls||clear')
        primeiro_jogar = input("Quer ser o primeiro a jogar? [s/n]: ").upper()
    """