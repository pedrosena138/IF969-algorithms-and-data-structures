# Estruturas de Dados
- Conjuntos são tão fundamentais para a ciência da computação quanto para a matemática. Enquanto os conjuntos matemáticos são invariáveis, os conjuntos manipulados por algoritmos podem crescer, encolher ou sofrer outras mudanças ao longo do tempo. Chamamos tais conjuntos de ***conjuntos dinâmicos***.
- Em uma implementação típica de um conjunto dinâmico, cada elemento é representado por um **objeto**. Alguns conjuntos dinâmicos consideram que um dos atributos do objeto é uma **chave de identificação**.
  > Ex.: O objeto contém dados satélites que não são utilizados pela implementação do conjunto dinâmico.
- Também podemos ter atributos que são manipulados pelas operações de conjuntos:
  > Chamados de ponteiros ou referências: Atributos que referenciam outros objetos no conjunto. Esses ponteiros localizam outros objetos na estrutura de dados.
- Algoritmos podem exigir a execução de vários tipos diferentes de operações em conjuntos:
  - Consultas - que simplesmente retornam informações sobreo conjunto (encontrar menores valores, valores maiores).
  - Operações Modificadoras - que alteram o conjunto (inserir, remover).
- Damos o nome de **dicionário** ao conjunto dinâmico que suporta essas operações.

## Estruturas de Dados Elementares 
### [Filas (Queues)](https://github.com/pedrosena138/IF969-Algoritmos-e-Estrutura-de-Dados/blob/master/Estruturas-de-Dados/Estruturas-Elementares/fila.py)
> Conjuntos dinâmicos nos quais os elemento são inseridos sempre no fim removidos sempre do início da estrutura (FIFO - First-In, First-Out).

- Inserção (enfileirar): ```fila.enqueue(x)```
- Remoção (desenfileirar): ```fila.dequeue()```

### [Pilhas (Stacks)](https://github.com/pedrosena138/IF969-Algoritmos-e-Estrutura-de-Dados/blob/master/Estruturas-de-Dados/Estruturas-Elementares/pilha.py)
> Conjuntos dinâmicos nos quais os elemento são sempre inseridos ou removidos no final da estrutura (LIFO - Last-In, First-Out)

- Inserção: ```pilha.push(x)```
- Remoção: ```pilha.pop()```

### Listas
- [**Listas Encadeadas**](https://github.com/pedrosena138/IF969-Algoritmos-e-Estrutura-de-Dados/blob/master/Estruturas-de-Dados/Estruturas-Elementares/lista-ligada.py)
  > É uma estrutura de dados na qual os objetos estão organizados em ordem sequencial.
  
  - Nos dão uma representação simples e flexível para conjuntos dinâmicos, suportando todas as operações (inserir, remover,...).
  - Entretanto, diferentemente de um vetor, no qual a ordem é determinada pelos índices do vetor (posição na memória), a ordem em uma lista ligada é determinada por um ponteiro em cada objeto.

  ![](https://github.com/pedrosena138/IF969-Algoritmos-e-Estrutura-de-Dados/blob/master/Estruturas-de-Dados/img/lista-encadeada.png)
  
- [**Listas Duplamente Encadeadas**](https://github.com/pedrosena138/IF969-Algoritmos-e-Estrutura-de-Dados/blob/master/Estruturas-de-Dados/Estruturas-Elementares/lista-duplamente-ligada.py)
  > Cada elemento de uma lista duplamente ligada L é um objeto com um atributo chave e dois outros atributos ponteiros: **próximo** e **anterior**.
  
  - O objeto também pode conter outros **dados satélites**.
  - Dado um elemento **x** na lista, **x.proximo** aponta para seu sucessor na lista ligada e **x.anterior** aponta para seu predecessor.
  - Se **x.anterior** = NULL, o elemento **x** não tem nenhum predecessor e, portanto, é o primeiro elemento, ou **início**, da lista.
  - Se **x.proximo**=NULL, o elemento **x** não tem nenhum sucessor e, assim, é o último elemento, ou **fim**, da lista.
  - Um atributo **L.inicio** aponta para o primeiro elemento da lista. Se
**L.inicio** é NULL então a lista está vazia.

  ![](https://github.com/pedrosena138/IF969-Algoritmos-e-Estrutura-de-Dados/blob/master/Estruturas-de-Dados/img/lista-duplament-encadeada.png)
  
## Árvores Binárias
> Árvores binárias são árvores em que cada nó possui no máximo dois filhos.

![](https://github.com/pedrosena138/IF969-Algoritmos-e-Estrutura-de-Dados/blob/master/Estruturas-de-Dados/img/arvore.PNG)

### Subárvore
> Árvores quem contém um nó e todos os seus descendentes.

![](https://github.com/pedrosena138/IF969-Algoritmos-e-Estrutura-de-Dados/blob/master/Estruturas-de-Dados/img/sub-arvore.PNG)

### Encaminhamento em Árvore
> Caminhamentos em árvore são diferentes formas de se percorrer os nós de uma árvore, baseiam-se na ordem em que a raiz é visitada com relação a seus descendentes. Têm normalmente o mesmo custo, a diferença está no efeito produzido, e muitas vezes, para uma situação há um caminhamento mais adequado.

- **Pré-Ordem**
  - A raiz é visitada antes dos seus descendentes. 
  - Depois as sub-árvores da raiz são visitadas em pré-ordem da esquerda para a direita.
```
Pre-Ordem(x):
  if x != NULL:
    print x.chave
    Pre-Ordem(x.esquerda)
    Pre-Ordem(x.direita)
```
- **Em-Ordem**
  - Visitar a sub-árvore à esquerda Em-ordem;
  - Visitar a raiz. (entre as sub-árvores);
  - Visitar a sub-árvore à direita Em-ordem.
```
Em-Ordem(x):
  if x != NULL:
    Em-Ordem(x.esquerda)
    print x.chave
    Em-Ordem(x.direita)
```
- **Pós-Ordem**
  - As sub-árvores da raiz são visitadas em pós-ordem da esquerda para a direita;
  - A raiz é visitada depois dos seus descendentes.
```
Pos-Ordem(x):
  if x != NULL:
    Pos-Ordem(x.esquerda)
    Pos-Ordem(x.direita)
    print x.chave
```

### [Árvores Binárias de Busca](https://github.com/pedrosena138/IF969-Algoritmos-e-Estrutura-de-Dados/blob/master/Estruturas-de-Dados/Arvores-Binarias/arvore-binaria-busca.py)
> Na árvore binária para busca, as chaves possuem uma organização estrutural.

- Seja **x** um nó em uma árvore de busca binária. Se **y** é um nó na subárvore esquerda de **x**, então **y.chave < x.chave**;
- Se **y** é um nó na subárvore direita de **x**, então **y.chave > x.chave**.

 Se os nós estão espalhados uniformemente, a consulta é rápida para grande quantidade de dados, divide-se o espaço de busca restante em dois em cada passo da busca: O(log2 n).
 
### [Árvores AVL](https://github.com/pedrosena138/IF969-Algoritmos-e-Estrutura-de-Dados/blob/master/Estruturas-de-Dados/Arvores-Binarias/arvore-avl.py)
> A árvore binária pode degenerar para uma estrutura próxima a uma lista ligada, e o tempo de acesso deixa de ser logarítmico.

![](https://github.com/pedrosena138/IF969-Algoritmos-e-Estrutura-de-Dados/blob/master/Estruturas-de-Dados/img/ex1-arvore.PNG)


Ex.: 50, 20, 39, 42, 40 ...

- **Solução: Manter todas as folhas mais ou menos na mesma altura**
  > Proposta em 1962 pelos matemáticos russos G.M. **A**delson-**V**elskki e E.M. **L**andis: métodos de inserção e remoção de elementos da árvore de forma que ela fique balanceada. Dessa forma a busca sempre será O(log2 n).

![](https://github.com/pedrosena138/IF969-Algoritmos-e-Estrutura-de-Dados/blob/master/Estruturas-de-Dados/img/propriedade-AVL.PNG)

- **Métodos de Balanceamento:**
  - Dinâmico: Mantém a árvore balanceada toda vez que é um nó é inserido ou removido.
  - Global (Estático): Permite à árvore crescer sem limites e somente faz o balanceamento quando tal necessidade é acionada, externamente.

- **Como é que se sabe quando é necessário balancear a árvore?**
  - Se a diferença de altura das subárvores deve ser 1, no máximo, então temos que procurar diferenças de altura maior do que isso;
  - Cada nó pode manter a diferença de altura de suas subárvores
    > Convencionalmente chamada de **fator de balanceamento** (FB) do nó

- **Controle de balanceamento**
1. Raiz de uma subárvore com FB -2 (ou 2) e um nó filho com FB -1 (ou 1)
    - Os fatores de balanceamento têm sinais iguais: subárvores de nó raiz e filho pendem para o mesmo lado;
    - Rotação simples para o lado oposto;
    - Às vezes, é necessário realocar algum elemento, pois ele perde seu lugar na árvore.
      
![](https://github.com/pedrosena138/IF969-Algoritmos-e-Estrutura-de-Dados/blob/master/Estruturas-de-Dados/img/ex2-part1-arvore.png)
![](https://github.com/pedrosena138/IF969-Algoritmos-e-Estrutura-de-Dados/blob/master/Estruturas-de-Dados/img/ex2-part2-arvore.png)

2. Raiz de uma subárvore com FB -2 (ou 2) e um nó filho com FB 1 (ou -1)
    - Os fatores de balanceamento têm sinais opostos: subárvore de nó raiz pende para um lado e subárvore de nó filho pende para o outro (ou o contrário);
    - Rotação dupla;
      >Primeiro, rotaciona-se o filho para o lado do desbalanceamento do pai. Em seguida, rotaciona-se o pai para o lado oposto do desbalanceamento
    - Às vezes, é necessário realocar algum elemento, pois ele perde seu lugar na árvore.
    
![](https://github.com/pedrosena138/IF969-Algoritmos-e-Estrutura-de-Dados/blob/master/Estruturas-de-Dados/img/ex3-part1-arvore.png)
![](https://github.com/pedrosena138/IF969-Algoritmos-e-Estrutura-de-Dados/blob/master/Estruturas-de-Dados/img/ex3-part2-arvore.png)
