"""
Universidade Federal de Pernanbuco - UFPE (www.ufpe.br)
Centro de Informática - CIn (www2.cin.ufpe.br)
Bacharelado em Sistemas de Informação
IF969 - Algoritmos e Estrutura de Dados

Autor: Pedro Manoel Farias Sena de Lima (pmfsl)
Email: pmfsl@cin.ufpe.br
Data: 2019-08-28
 
Copyright © 2019 todos os direitos reservados

Descrição: Utilizacao de super classes
"""

class Empreendimento:
    def __init__(self, nome, cnpj, endereco):
        pass
    
    def getNome(self):
        pass
    
    def getEndereco(self):
        pass

    def getCnpj(self):
        pass
    
    def getSaldo(self):
        pass
    
    def setNome(self, nome):
        pass
    
    def setEndereco(self, endereco):
        pass
    
    def setCnpj(self, cnpj):
        pass
    
    def setVenda(self, venda):
        pass

class Supermercado(Empreendimento):
    def __init__(self, nome, cnpj, endereco):
        self.nome = nome
        self.cnpj = cnpj
        self.endereco = endereco
        self.saldo = float()
    
    def getNome(self):
        return self.nome
    def setNome(self, nome):
        self.nome = nome
    
    def getEndereco(self):
        return self.endereco
    def setEndereco(self, endereco):
        self.endereco = endereco

    def getCnpj(self):
        return self.cnpj
    def setCnpj(self, cnpj):
        self.cnpj = cnpj

    def getSaldo(self):
        return self.saldo
    
    def setVenda(self, venda):
        self.saldo += venda

def main():
    listaEmp = list()
    
    nome = input("Insira o nome: ")
    endereco = input("Insira o endereco: ")
    cnpj = input("Insira o cnpj: ")
    mercado01 = Supermercado(nome, cnpj, endereco)
    listaEmp.append(mercado01)
    print("")
    
    nome = input("Insira o nome: ")
    endereco = input("Insira o endereco: ")
    cnpj = input("Insira o cnpj: ")
    mercado02 = Supermercado(nome, cnpj, endereco)
    listaEmp.append(mercado02)
    print("")
    
    nome = input("Insira o nome: ")
    endereco = input("Insira o endereco: ")
    cnpj = input("Insira o cnpj: ")
    mercado03 = Supermercado(nome, cnpj, endereco)
    listaEmp.append(mercado03)

    print("\n---Empreendimentos---")
    for emp in listaEmp:
        if input("Houve alguma venda? [s/n]: ") == "s":
            venda = float(input("Insira o valor da venda: R$"))
            emp.setVenda(venda)
        print("Nome: {}"
            "\nCNPJ: {}"
            "\nEndereco: {}"
            "\nSaldo: R${}" .format(emp.getNome(), emp.getCnpj(), emp.getEndereco(), emp.getSaldo()))
        print("")

if __name__ == "__main__":
    main()