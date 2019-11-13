#-*- coding: utf-8 -*-
import textwrap
from lista import Lista
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
        self.__valor = float()
    
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
        return self.__valor
    def setValor(self, valor):
        self.__valor = valor 
    
    def __str__(self):
        saida = '{} -- {} -- {} -- Descricao: {}' .format(str(self.__cod_tipo), self.__desc_tipo, str(locale.currency(self.__valor, grouping=True)), textwrap.wrap(self.__desc_bem, 80))
        return saida
    
    def __repr__(self):
        atributos = (self.__cod_tipo, self.__desc_tipo, self.__valor, self.__desc_bem)
        return str(atributos)
    
    def __getTipo(self, outro):
        if type(self) == type(outro):
            return True
        else:
            raise TypeError('Operacao nao suportada entre as instancias dos objetos')

    def __lt__(self, bem):
        if self.__getTipo(bem):
            return (self.__valor < bem.getValor() or self.__cod_tipo < bem.getCodigo() or self.__desc_bem < bem.getDescBem())

    def __gt__(self, bem):
        if self.__getTipo(bem):
            return (self.__valor > bem.getValor() or self.__cod_tipo > bem.getCodigo() or self.__desc_bem > bem.getDescBem())
    
    def __le__(self, bem):
        if self.__getTipo(bem):
            return (self.__valor <= bem.getValor() or self.__cod_tipo <= bem.getCodigo() or self.__desc_bem <= bem.getDescBem())
    
    def __ge__(self, bem):
        if self.__getTipo(bem):
            return (self.__valor >= bem.getValor() or self.__cod_tipo >= bem.getCodigo() or self.__desc_bem >= bem.getDescBem())
    
    def __eq__(self, bem):
        if self.__getTipo(bem):
            return ((self.__valor == bem.getValor()) and (self.__desc_bem == bem.getDescBem()))
           
    def __ne__(self, bem):
        if self.__getTipo(bem):
            return ((self.__valor != bem.getValor()) or (self.__desc_bem != bem.getDescBem()))

if __name__ == "__main__":
    lista = Lista()
     
    bem1 = Bem()
    bem1.setValor(1400.79)
    bem1.setCodigo(1)
    bem1.setDescBem('cadeira')
    bem1.setDescTipo('movel')
    
    bem2 = Bem()
    bem2.setValor(70)
    bem2.setCodigo(2)
    bem2.setDescBem('banco')
    bem2.setDescTipo('movel')
    
    bem3 = Bem()
    bem3.setValor(100)
    bem3.setCodigo(3)
    bem3.setDescBem('hilux')
    bem3.setDescTipo('carro')
    
    lista.Inserir(bem1)
    lista.Inserir(bem2)
    lista.Inserir(bem3)

    u = bem1
    u.setValor(1000.43)
    print(u)
    print(bem1)

    

    