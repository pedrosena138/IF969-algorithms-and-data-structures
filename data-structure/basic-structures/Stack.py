class Node():
    def __init__(self,dado):
        self.dado = dado
        self.primeiro = None
        self.anterior = None

    
class Pilha:
    def __init__(self):
        self.primeiro = Node

    def remover(self,no):
        
        self.ultimo = self.primeiro
        self.primeiro = no(None)
    
    def inserir(self,no):
        self.primeiro = self.ultimo
        self.ultimo = no
   

    def desempilha(self):
        elemento = self.ultimo

        if elemento.anterior == None:
            return None
        else:
            dado = elemento.dado
            self.ultimo = elemento.anterior
            del elemento
            return dado



pilha = Pilha()


pilha.inserir(1)
print(pilha)

        
        
    





