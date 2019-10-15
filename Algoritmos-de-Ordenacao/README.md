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
- Dois dos métodos são baseados numa técnica de desenho de algoritmos chamada *dividir e conquistar*;
- Essa técnica baseia-se na divisão do problema em problemas menores, mais fáceis de resolver;
- As soluções dos problemas menores são combinadas para resolver o problema maior.

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

### [Shellsort](https://github.com/pedrosena138/IF969-Algoritmos-e-Estrutura-de-Dados/blob/master/Algoritmos-de-Ordenacao/ordenacao-basica/shellsort.py)
- A escolha da ótima sequência de valores para h é desconhecida. Foi mostrado por Knuth que a seguinte sequência fornece bons
resultados:
  > Sequência: 1, 4, 13, 40, 121, 364, 1093, 3280 ...
  ```
  h(1) = 1
  H(s) = 3*h(s-1) + 1
  ```
- Assim, escolhe-se inicialmente o maior valor h(s) tal que esse seja menor que N. Depois se escolhe os valores anteriores da
sequência;
- A complexidade do algoritmo depende da sequência escolhida. Existem vários estudos mostrando a complexidade com diferentes sequências;
- Sedgewick faz uma análise dos limites inferior e superior em http://www.cs.princeton.edu/~rs/shell/paperF.pdf (acessado
2019-10-15);
- O algoritmo possui bom desempenho para vetores de tamanhos moderados, mas é inferior a outros algoritmos;
- Podem ocorrer muitos cache misses devido à natureza do algoritmo, o que afeta seu desempenho real em computadores modernos.

![](https://upload.wikimedia.org/wikipedia/commons/d/d8/Sorting_shellsort_anim.gif)

## Ordenação Avançada

### [Mergesort](https://github.com/pedrosena138/IF969-Algoritmos-e-Estrutura-de-Dados/blob/master/Algoritmos-de-Ordenacao/ordenacao-avancada/mergesort.py)
- C(N) = O(N.lg(N))
- A(N) = Θ(N)
- M(N) = O(N) (para cada sub-vetor)
- Dividir um vetor em duas metades;
- Ordenar cada uma das metades (aplicar o algoritmo recursivamente);
- Combinar as metades para formar o vetor ordenado
- O algoritmo requer espaço adicional para combinar as metades ordenadas;
- Como são feitas muitas intercalações, é preferível trabalhar com apenas um vetor auxiliar do mesmo tamanho do vetor original;
- Intercalações são feitas no vetor auxiliar e copiadas de volta para o original.

![](https://thumbs.gfycat.com/NaturalWelloffGalago-size_restricted.gif)

### [Quicksort](https://github.com/pedrosena138/IF969-Algoritmos-e-Estrutura-de-Dados/blob/master/Algoritmos-de-Ordenacao/ordenacao-avancada/quicksort.py)
- Melhor caso:
  - C(N) = O(N.lg(N))
  - M(N) = O(N)
- Pior caso:
  - C(N) = O(N²)
  - M(N) = O(N²)
- A ideia é similar ao [mergesort](https://github.com/pedrosena138/IF969-Algoritmos-e-Estrutura-de-Dados/blob/master/Algoritmos-de-Ordenacao/README.md#mergesort), contudo não requer espaço adicional de armazenamento além da pilha de execução;
- Também é um algoritmo dividir e conquistar. O vetor é particionado em dois subvetores conforme um elemento qualquer chamado *pivô*:
  - Esquerda contém os elementos menores que o pivô
  - Direita contém os elementos maiores que o pivô
- O algoritmo é aplicado a cada um dos subvetores e, ao terminar, o vetor encontra-se ordenado.

![](https://thumbs.gfycat.com/RectangularHarmlessGalapagosmockingbird-size_restricted.gif)
