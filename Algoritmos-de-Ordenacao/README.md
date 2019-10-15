# Algoritmos de Ordenação
- Knuth observou que nos anos 1960 fabricantes de computadores estimavam que 25% do tempo de computação era gasto em ordenação.
- A necessidade de apresentar informações ordenadas é inquestionável. Ordenação também é necessária para construção de outros
algoritmos.
  > Por exemplo: busca binária
- Algoritmos de ordenação estão divididos em duas grandes categorias:
  - Baseados em comparações;
  - Baseados em distribuição.
- Também são divididos em:
  - Ordenação interna (em memória principal);
  - Ordenação externa (em memória secundária).
- Ordenação é feita com base numa chave (parte do item ou externa). Supõe-se uma ordem total sobre as chaves:
  - Antissimétrica (c1 < c2 e c2 < c1 -> c1 = c2)
  - Transitiva ( c1 < c2 e c2 < c3 -> c1 < c3)
  - Total (c1 < c2 ou c2 < c1 para toda chave c1, c2)
- Um algoritmo é **estável** se a ordem relativa dos elementos iguais é mantida após a ordenação
  > Ordenar lista alfabética de alunos pela nota final
- Análise dos algoritmos baseados em comparação leva em conta:
  - Número de comparações, C(N)
  - Número de trocas (movimentações), M(N)
  - Memória adicional, A(N)
  
## Ordenação Básica
### [Bubblesort](https://github.com/pedrosena138/IF969-Algoritmos-e-Estrutura-de-Dados/blob/master/Algoritmos-de-Ordenacao/ordenacao-basica/bubblesort.py)
- C(N) = O(N²) 
- M(N) = O(N²)
- Repetidas trocas entre elementos consecutivos;
- Se elemento maior que próximo, trocar;
- Elementos maiores ‘flutuam’ em direção ao fim do vetor;
- Péssimo desempenho;
- Estável;
- Custo independe se vetor está (parcialmente) ordenado;
- Fácil implementação. Útil para poucos itens.

![](https://upload.wikimedia.org/wikipedia/commons/0/06/Bubble-sort.gif)

### [Selectionsort](https://github.com/pedrosena138/IF969-Algoritmos-e-Estrutura-de-Dados/blob/master/Algoritmos-de-Ordenacao/ordenacao-basica/selectionsort.py)
- C(N) = O(N²)
- M(N) = O(N)
- Outro algoritmo exaustivo como [bubblesort](https://github.com/pedrosena138/IF969-Algoritmos-e-Estrutura-de-Dados/blob/master/Algoritmos-de-Ordenacao/README.md#bubblesort);
- Encontrar menor elemento do vetor;
- Trocá-lo com o primeiro elemento;
- Desconsiderar menor elemento;
- Repetir processo para os demais;
- Simples de implementar;
- Poucas trocas (útil para casos em que os itens são grandes);
- Não estável;
- Custo independe se vetor está (parcialmente) ordenado.
![](https://thumbs.gfycat.com/SnappyMasculineAmericancicada-size_restricted.gif)

### [Insertionsort](https://github.com/pedrosena138/IF969-Algoritmos-e-Estrutura-de-Dados/blob/master/Algoritmos-de-Ordenacao/ordenacao-basica/insertionsort.py)
- Melhor caso - Elemento encontra-se na posição correta, 1 única comparação:
  - C(N) = O(N)
  - M(N) = O(N)
- Pior caso:
  - C(N) = O(N²)
  - M(N) = O(N²)
- Dividir vetor entre ordenados (à esquerda) e a ordenar (à direita);
- Inserir primeiro elemento da direita na subsequência ordenada da esquerda;
- Repetir processo até que todos tenham sido avaliados;
- Processo similar a ordenar cartas na mão.

![](https://upload.wikimedia.org/wikipedia/commons/9/9c/Insertion-sort-example.gif)

## Ordenação Avançada
