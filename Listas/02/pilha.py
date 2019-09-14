'''
Universidade Federal de Pernambuco - UFPE (www.ufpe.br)
Centro de Informática - CIn (www2.cin.ufpe.br) 
Bacharelado em Sistemas de Informação 
IF969 - Algoritmos e Estrutura de Dados 
Professor: Hansenclever Bassani 
Autor: Pedro Manoel Farias Sena de Lima (pmfsl)
Email: pmfsl@cin.ufpe.br
Data: 2019-09-14
Copyright © 2019 todos os direitos reservados
Descricao: Implementacao de uma Pilha.
'''

from base import ListaDupla

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

    print("\nIndice do 'o' na Pilha:",pilha.Indice('o'))
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