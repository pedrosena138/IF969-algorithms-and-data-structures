from lista import ListaDupla

class Pilha(ListaDupla):
    def __init__(self, item=None):
        super().__init__(item)
    
    def Push(self, item):
        super().Anexar(item)
    
    def Pop(self):
        if not(self.Vazia()):
            no_anterior = self._ListaDupla__fim.getAnterior()
            self._ListaDupla__fim.setAnterior(None)
            if not(no_anterior is None): no_anterior.setProximo(None)
            self._ListaDupla__fim = no_anterior
    
    def Inserir(self, chave, item):
        raise NotImplementedError('Pilha() nao possui funcao Inserir()')

    def Selecionar(self, chave, item):
        raise NotImplementedError('Pilha() nao possui funcao Selecionar()')

def main():
    pilha = Pilha('algoritmos')
    print(pilha)

    pilha.Push('O')
    print(pilha)

    pilha[3] = 'U'
    print(pilha)

    pilha.Pop()
    print(pilha)

    pilha2 = Pilha('Pilha')
    pilha.Concatenar(pilha2)
    print('\nA Pilha tem {} elemento(s)' .format(len(pilha)))
    print(pilha)

if __name__ == "__main__":
    main()