"""
Universidade Federal de Pernanbuco - UFPE (www.ufpe.br)
Centro de Informática - CIn (www2.cin.ufpe.br)
Bacharelado em Sistemas de Informação
IF969 - Algoritmos e Estrutura de Dados

Autor: Pedro Manoel Farias Sena de Lima (pmfsl)
Email: pmfsl@cin.ufpe.br
Data: 2019-08-28
 
Copyright © 2019 todos os direitos reservados

Descrição: Criar uma classe Aluno com os métodos inicializarNota(nota,numeroProva), verificaSituacaoMedia(),
imprimeInformacoes().
"""

class Aluno:
    def __init__(self, nome, cpf, quantNotas):
        self.__cpf = cpf
        self.__nome = nome
        self.__listaNotas = list()
        self.__quantNotas = quantNotas
        
        for i in range(self.__quantNotas):
            self.__listaNotas.append(None)

    def inicializarNota(self, nota, index):
        self.__listaNotas[index] = nota
    
    def notasPreenchidas(self):
        for i in self.__listaNotas:
            if i == None:
                print("Nota %i não informada" % (self.__listaNotas.index(i)+1))
                return False
            else:
                return True
                
    def verificaSituacaoMedia(self):
        media = sum(self.__listaNotas)/len(self.__listaNotas)
        if media >= 7.0:
            return True
        elif not(self.notasPreenchidas()) or media < 7.0:
            return False
    
    def imprimiInformacoes(self):
        if self.notasPreenchidas():
            print("Nome: {}, CPF: {}" .format(self.__nome, self.__cpf))
            for i in self.__listaNotas:
                print("Nota{}: {}" .format((self.__listaNotas.index(i)+1), i))

def main():
    quantNotas = int(input("Quantidade de notas: "))
    aluno = Aluno("Pedro", "123456789", quantNotas)

    for i in range(quantNotas):
        nota = float(input("Nota %i: " % (i+1)))
        aluno.inicializarNota(nota, i)
    
    print("")
    aluno.imprimiInformacoes()

    if aluno.verificaSituacaoMedia():
        print("Aluno aprovado!!!")
    else:
        print("Aluno reprovado!!!")

if __name__ == "__main__":
    main()


    

