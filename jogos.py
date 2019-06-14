import os

def misere():
    escolha_j = str()  # escolha do jogador
    escolha_c = str()  # escolha do computador
    primeiro_jogar = str()  # primeiro a jogar (jogador ou computador

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

def notakto():
    print("jogando notakto")