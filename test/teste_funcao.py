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

def fim_jogo(posicoes, humano, computador):
    """
    Funcao que verifica se o computador ou humano venceu
    param posicoes: posicoes atuais no tabuleiro
    param jogador: HUMANO ou COMPUTADOR
    """
    return estado_vitoria(posicoes, humano) or estado_vitoria(posicoes, computador)

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

def jogadas(jogador, posicoes, ia):

    while not movimento_valido(jogador-1, posicoes):
        try:
            jogador = int(input("Escolha uma casa [1 a 9]: "))
        except (KeyError, ValueError):
            print('Insira um valor. ', end='')
    return jogador
    
def notakto(modo_normal):
    H = -1 #Humano
    C = +1 #Computador
    posicoes = [0,0,0,0,0,0,0,0,0] #posicoes no tabuleiro
    jogada_h = int() #jogada do humano
    jogada_c = int() #jogada do computador

    print("========================================")
    print("                NOTAKTO                 ")
    print("========================================")
    

    while len(celulas_vazias(posicoes)) > 0 and not fim_jogo(posicoes, H, C):
        tabuleiro(posicoes, modo_normal)
        jogada_h = jogadas(jogada_h,posicoes)
        posicoes[jogada_h-1] = 1
    tabuleiro(posicoes, modo_normal)

notakto(False)