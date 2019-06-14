import os

posicoes = [0,0,0,0,0,0,0,0,0] #tabuleiro
escolha_h = int() #escolha do humano
escolha_c = int() #escolha do computador
inicia_jogo = bool() #escolha de quem irá começar jogando

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
            
            if posicoes[x] != 0:
                print(f'\t|  X  |', end='')
            else:
                print(f'\t|     |', end='')
        print("\n" + divisor) 

def jogadores(humano, computador, modo_normal):
    """
    Funcao para definicao dos jogadores
    param humano: seta as definicoes do humano
    param computador: seta as definicoes do computador
    param modo_normal: define se o jogo vai ser jogado com 'X e O' ou so 'X'
    """

def notakto():
    tabuleiro(posicoes, False)
    print("jogando notakto")

def misere():
    tabuleiro(posicoes, True)
    print("jogando misere")
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