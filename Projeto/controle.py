#-*- coding: utf-8 -*-
'''
Classe principal do programa
'''

def carregar_candidatos(arquivo):
    '''
    Carrega os candidatos a partir de um arquivo e os armazena em objetos do tipo Candidato(),
    esses objetos sao armazenados em uma classe Lista()
    '''
    raise NotImplementedError()

def carregar_bens(arquivo):
    '''
    Carrega os bens dos candidatos a partir de um arquivo e os armazena em objetos do tipo Bem(),
    esses objetos sao armazenados em uma classe Lista()
    '''
    raise NotImplementedError()

def lista_candidatos():
    '''
    Retorna os candidatos de acordo com certas condicoes
    '''
    raise NotImplementedError()

def exibir_lista():
    '''
    Exibi a lista obtida no metodo lista_candidatos()
    '''
    raise NotImplementedError()

def media_bens():
    '''
    Mostra amostram a media do total de bens dos candidatos por cargo, UF, partido, ocupacao, 
    ou ano de nascimento.
    '''
    raise NotImplementedError()

def remover_lista():
    '''
    Funcao que remove da lista todos os candidatos que satisfacam um critério.
    '''
    raise NotImplementedError()

def main():
    raise NotImplementedError()

if __name__ == "__main__":
    main()