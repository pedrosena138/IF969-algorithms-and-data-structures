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
Descricao: Implementacao de uma Fila.
'''

from base import ListaDupla

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

def main():
    fila = Fila('algoritmos')
    print(fila)

    fila.Enqueue('O')
    print(fila)

    print("\nIndice do 's' na Fila:",fila.Indice('s'))
    fila[9] = 'S'
    print(fila)

    fila.Dequeue()
    print(fila)

    fila2 = Fila('fila')
    fila.Concatenar(fila2)
    print('\nA Fila tem {} elemento(s)' .format(len(fila)))
    print(fila)
    
if __name__ == "__main__":
    main()
