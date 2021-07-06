"""
Universidade Federal de Pernanbuco - UFPE (www.ufpe.br)
Centro de Informática - CIn (www2.cin.ufpe.br)
Bacharelado em Sistemas de Informação
IF969 - Algoritmos e Estrutura de Dados

Autor: Pedro Manoel Farias Sena de Lima (pmfsl)
Email: pmfsl@cin.ufpe.br
Data: 2019-08-28
 
Copyright © 2019 todos os direitos reservados

Descrição: Compara dois objetos de classe Programa
"""

class Programa:
    def __init__(self, anoCriacao, codigo, dono, email, numLinhas):
        self.anoCriacao = anoCriacao
        self.codigo = codigo
        self.dono = dono
        self.emailDono = email
        self.numLinhas = numLinhas
    
    def getAnoCriacao(self):
        return self.anoCriacao
    def setAnoCriacao(self, ano):
        self.anoCriacao = ano
    
    def getCodigo(self):
        return self.codigo
    def setCodigo(self, codigo):
        self.codigo = codigo
    
    def getDono(self):
        return self.dono
    def setDono(self, dono):
        self.dono= dono
    
    def getEmailDono(self):
        return self.emailDono
    def setEmailDono(self, email):
        self.emailDono = email
    
    def getNumLinhas(self):
        return self.numLinhas
    def setNumLinhas(self, linhas):
        self.numLinhas = linhas
    
    def calculaNumLinhas(self):
        self.setNumLinhas(self.codigo.count('\n')+1)
    
    def calculaIdadeCodigo(self, ano):
        return ano - self.anoCriacao

def comparaCodigo(programa1, programa2):
    return programa1.getCodigo() == programa2.getCodigo()

def main():
    programa1 = Programa(2013, "a=1\nb=2\nreturn True", "Joao", "joao@cin.ufpe", 3)
    programa2 = Programa(2014, "a=1\nb=2\nc=3\nreturn True", "Maria", "maria@cin.ufpe", 4)

    print("Linhas programa1:" + str(programa1.getNumLinhas()))
    print("Linhas programa2:" + str(programa2.getNumLinhas()))

    if comparaCodigo(programa1, programa2):
        print("O programa1 é igual ao programa2")
    else:
        print("O programa1 é diferente do programa2")

    programa2.setCodigo("a=1\nb=2\nreturn True")
    programa2.calculaNumLinhas()

    print("Linhas programa1:" + str(programa1.getNumLinhas()))
    print("Linhas programa2:" + str(programa2.getNumLinhas()))

    if comparaCodigo(programa1, programa2):
        print("O programa1 é igual ao programa2")
    else:
        print("O programa1 é diferente do programa2")

if __name__ == "__main__":
    main()