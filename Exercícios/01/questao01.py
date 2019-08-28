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
    def __init__(self, nome, cpf):
        self.cpf = cpf
        self.nome = nome
        self.nota1 = self.nota2 = self.nota3 = None

    def inicializarNota(self, nota, index):
        if index == 1:
            self.nota1 = nota
        elif index == 2:
            self.nota2 = nota
        elif index == 3:
            self.nota3 = nota
    
    def notasPreenchidas(self):
        if self.nota1 == None:
            print("Nota 1 nao inicializada")
            return False
        if self.nota2 == None:
            print("Nota 2 nao inicializada")
            return False
        if self.nota3 == None:
            print("Nota 3 nao inicializada")
            return False
        
        return True
                
    def verificaSituacaoMedia(self):
        if not self.notasPreenchidas:
            return False
        else:
            if ((self.nota1+self.nota2+self.nota3)/3) >= 7.0:
                return True
            else:
                return False
    
    def imprimiInformacoes(self):
        if self.notasPreenchidas():
            print("Nome: %s, CPF: %s, Nota 1: %f, Nota 2: %f, Nota 3: %f" %
             (self.nome, self.cpf, self.nota1, self.nota2, self.nota3))

def main():
    aluno = Aluno("Pedro", "123456789")

    aluno.inicializarNota(4.6,1)
    aluno.inicializarNota(8,2)

    aluno.imprimiInformacoes()
        
    aluno.inicializarNota(6.4,3)
    if aluno.verificaSituacaoMedia():
        print("Aluno aprovado!!!")
    else:
        print("Aluno reprovado!!!")
    print("")
    aluno.imprimiInformacoes()

    

if __name__ == "__main__":
    main()


    

