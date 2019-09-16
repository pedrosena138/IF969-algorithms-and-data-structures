# Lista 02 - Fila, Lista e Pilha

**1. Implemente uma classe de _Lista Duplamente Encadeada_. Sua implementação deve atender aos seguintes requisitos:**  
**a.** O método construtor da classe deve poder receber, opcionalmente, um objeto iterável, de modo que, quando receber esse objeto, a lista seja criada a partir dele. Por exemplo:
  * Entrada  
    ```
    lista = ListaDuplamenteEncadeada(‘algoritmos’)  
    print(lista)
    ```
  * Saída  
  ```>> “a, l, g, o, r, i, t, m, o, s”```  
  
 **b.** Implemente os métodos a seguir:  
   * ```__str__```: Deve retornar uma string cujo valor represente o estado do objeto. Nesse caso, a string deve conter os elementos do primeiro ao último nó válido separados por vírgula;
   * ```__repr__```: Deve retornar uma string cujo valor represente o estado do objeto e possa ser usado como inicializador válido de uma instância de igual valor;
   * ```__getitem__```: Esse é o método responsável pela indexação da lista. Esse método recebe apenas um parâmetro, este é o índice do elemento a serbuscado. É esse o método chamado quando, com uma lista de Python, por exemplo, você acessa o elemento em um dado índice usando colchetes. Esse método deve levantar a exceção ‘IndexError’ caso seja fornecido umíndice que não pertence a lista;
   * ```__setitem__```: Assim como o modo anterior, este método também usado para cessar itens através de indexação, com a diferença de que esse método também é responsável pela mudança de valor do elemento na posição dada. É esse o método responsável pelo comportamento de associação de um elemento. Por exemplo: ```Lista[0] = 3```;  
   * ```indice```: Esse método deve receber um valor e procurar por ele na lista, retornando o índice do valor encontrado. Caso o valor seja não esteja contido na lista, o método deve levantar a exceção ```ValueError```.
   * ```anexar```: O método anexar deve funcionar exatamente como o método ```append```, da lista de Python;
   * ```selecionar```: O método selecionar funciona como o método pop da lista. Isto é, ele deve remover um elemento e retornar o valor do elemento removido;
   * ```inserir```: Esse método representa a inserção ordenada na lista. Ele recebe dois elementos, um índice e um valor, e deve ser inserido na posição informada, empurrando o elemento a sua direita e seus sucessores para a direita;
   * ```concatenar```: recebe como parâmetro uma outra lista duplamente encadeada e adiciona os elementos dessa lista ao fim, mantendo a ordem anterior. Por Exemplo:  
      * Entrada
        ```
        l1 = [1, 2, 3, 4]
        l2 = [5, 6, 7, 8]
        l1.concatenar(l2)
        print(l1)
        print(l2)
        ```
      * Saída
        ```
        >> [1, 2, 3, 4, 5, 6, 7, 8]
        >> []
        ```   
   * ```__iter__``` e ```__next__```: Esse é o método responsável por tornar um objeto iterável. É esse o método responsável pelo comportamento de um ```for``` numa llista. Embora Python possa tentar usar o for através de indexação sucessiva, isto é, usando valores de 0 até o valor limite na chamada do métoodo ```__getitem__```, em uma lista encadeada a complexidade dessa abordagem é de n!, uma vez que o método ```__getitem__``` equivale a percorrer a lista uma vez para cada elemento. Para aliviar essa complexidade usa-se o auxílio de um objeto iterador, que para esse exemplo chamaremos de ponteiro. Siga o passo-a-passo e você não deve encontrar problemas:
      * Defina uma classe Ponteiro que receba como parâmetro uma lista.
      * No método construtor do Ponteiro separe um atributo para guardar o valor do primeiro nó da lista. Você pode chamá-lo de posição, índice, passo...
      * Defina o método ```__next__``` no ponteiro. Esse método deve guardar o valor do nó para o qual ele aponta no momento, mover-se para o nó seguinte e retornar o valor guardado.
      * Implemente uma forma de identificar o último nó e, ao chamar o método ```__next__``` nele, faça com que o Python levante a exceção
```StopIteration```. Use a keyword ```raise``` para isso.  

**2. Por fim, implemente a classe _Fila_ e a classe _Pilha_ como subclasse direta da classe _Lista Duplamente Encadeada_. Lembre-se das diferenças de comportamento entre estruturas de dado LIFO e FIFO. Caso identifique algum método que não deve existir, defina o comportamento do método para apenas retornar o valor** ```None```**.**  
> Para sobrescrever um método derivado de uma classe pai, basta definir o método novamente na classe filha.
