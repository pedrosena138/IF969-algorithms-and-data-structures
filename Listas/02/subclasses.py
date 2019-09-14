from lista import ListaDupla

class Fila(ListaDupla):
    def __init__(self, item=None):
        super().__init__(item)
    
    def Enqueue(self, item):
        super().Anexar(item)
    
    def Dequeue(self):
        if not(self.Vazia()):
            
            no_proximo = self._ListaDupla__comeco.getProximo()
            self._ListaDupla__comeco.setProximo(None)
            if not(no_proximo is None): no_proximo.setAnterior(None)
            self._ListaDupla__comeco = no_proximo

    def Inserir(self, chave, item):
        raise NotImplementedError('Fila() nao possui funcao Inserir')

    def Selecionar(self, chave, item):
        raise NotImplementedError('Fila() nao possui funcao Selecionar()')

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
    fila = Fila('oi')
    pilha = Pilha('ola')

    pilha.Push('i')
    fila.Enqueue('i')

    pilha.Pop()
    fila.Dequeue()
    print(fila)
    print(pilha)

if __name__ == "__main__":
    main()