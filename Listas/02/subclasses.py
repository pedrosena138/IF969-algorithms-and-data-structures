from lista import ListaDupla

class Fila(ListaDupla):
    raise NotImplementedError()

class Pilha(ListaDupla):
    raise NotImplementedError()

def main():
    fila = Fila()
    pilha = Pilha()

    print(fila)
    print(pilha)

if __name__ == "__main__":
    main()