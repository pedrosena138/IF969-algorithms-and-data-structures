import os

tabuleiro = [0,0,0,0,0,0,0,0,0]
humano = 1
computador = -1

def avaliacao(estado):
    """
    Funcao para avaliar o estado o tabuleiro
    parametro estado: estado atual do tabuleiro
    """
    #retorna +1 se o computador ganhar
    if vitoria(estado, computador):
        pontuacao = +1
    #retorna -1 se o humano ganhar
    elif vitoria(estado,humano):
        pontuacao = -1
    #retorna 0 se for empate
    else:
        pontuacao = 0
    
    return pontuacao

def vitoria(estado, jogador):
    pass

def misere():
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

def notakto():
    print("jogando notakto")