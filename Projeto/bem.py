#-*- coding: utf-8 -*-
import textwrap
import locale
locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')

'''
Arquivo com a classe Bem()
'''

class Bem:
    def __init__(self):
        self.__cod_tipo = int()
        self.__desc_tipo = str()
        self.__desc_bem = str()
        self.__valor_bem = float()
    
    def getCodigo(self):
        return self.__cod_tipo
    def setCodigo(self, codigo):
        self.__cod_tipo = codigo
    
    def getDescTipo(self):
        return self.__desc_tipo
    def setDescTipo(self, descricao):
        self.__desc_tipo = descricao

    def getDescBem(self):
        return self.__desc_bem
    def setDescBem(self, descricao):
        self.__desc_bem = descricao
    
    def getValor(self):
        return self.__valor_bem
    def setValor(self, valor):
        self.__valor_bem = valor 
    
    def __str__(self):
        saida = '{} -- {} -- {} -- Descricao: {}' .format(str(self.__cod_tipo), self.__desc_tipo, str(locale.currency(self.__valor_bem, grouping=True)), textwrap.wrap(self.__desc_bem, 80))
        return saida
    
    def __repr__(self):
        return str((self.__cod_tipo, self.__desc_tipo, self.__valor_bem, textwrap.wrap(self.__desc_bem, 80)))