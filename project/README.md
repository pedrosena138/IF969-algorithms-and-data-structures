# Projeto IF969
> Programa para processar os dados dos candidatos e seus bens declarados à Justiça Eleitoral para o pleito de 2014, utilizando conceitos 
referentes a listas encadeadas e orientação à objetos.

## Classe Candidato()
> Classe que representa o candidato do pleito das eleições de 2014.

### Atributos
> Os atributos da classe devem ser obrigatoriamente privados. Dessa forma, deverão ser implementados métodos para acessar (alterar e obter)
os valores desses atributos.

- [x] Ano da eleição
- [x] Sigla da UF
- [x] Código do Cargo
- [x] Descrição do cargo
- [x] Nome do candidato
- [x] ID do candidato (número sequencial do candidato gerado pelos sistemas eleitorais)
- [x] Número na urna
- [x] CPF
- [x] Nome na urna
- [x] Número do partido
- [x] Nome do partido
- [x]  Sigla do partido
- [x] Código de ocupação do candidato
- [x] Descrição da ocupação
- [x] Data de nascimento (armazenada como dia, mês e ano)
- [x] Sexo do candidato
- [x] Grau de instrução
- [x] Estado civil
- [x] UF nascimento
- [x] Nome do município de nascimento
- [x] Situação do candidato pós pleito (eleito, não eleito, suplente)
- [x] Situação da candidatura (deferida ou indeferida)
- [x] Lista de bens

### Métodos
- [x] **incluirBens**: Recebe como parâmetro um objeto do tipo ```Bem``` e deve inseri-lo na *lista de bens do candidato*.
- [x] ```__str__```
- [x] ```__repr__```

### Output
```
Nome da Urna -- Número da Urna -- Sigla do partido
Cargo disputado (UF) Município Nascimento (UF)
Resumo dos bens:
   - Total declarado: (valor formatado como R$)
   - Total por tipo de bem (imprimir Tipo: valor formatado em R$)
```

## Classe Bem()
> Os bens declarados de cada candidato deverão ser armazenados em objetos do tipo Bem.

### Atributos
> Os atributos deverão ser todos privados. Dessa forma, você deverá implementar métodos de acesso aos valores armazenados.

- [x] Código do tipo de bem
- [x] Descrição do tipo de bem
- [x] Descrição detalhada do bem
- [x] Valor do bem

### Métodos
- [x] ```__str__```
- [x] ```__repr__```
- [x] **Métodos de comparação**: A comparação é baseada no valor do bem. Os critérios de desempate são: primeiro o código do bem;
segundo a descrição detalhada do bem. Dois bens são iguais se possuírem o mesmo valor e a mesma descrição detalhada.

### Output
```
Código -- Descrição do tipo -- Valor (formatado em R$) Descrição: Descrição detalhada
```

(A palavra descrição deve ser impressa e o texto da descrição deve ser formatado de maneira a não exceder 80 caracteres por linha; ver 
TextWrap)

## Classe Lista()
> Uma [lista duplamente encadeada](https://github.com/pedrosena138/IF969-Algoritmos-e-Estrutura-de-Dados/tree/master/Estruturas-de-Dados#listas) que armazena objetos.

### Métodos
- [x] **Inserir**: insere um elemento de forma ordenada
- [x] **Comparação**: Essa função de comparação deve possuir dois parâmetros (os objetos a serem comparados) e deve retornar -1, 0 ou 1 caso o primeiro objeto seja menor, igual, ou maior que o segundo objeto, respectivamente.
- [x] Métodos para exibição do conteúdo na tela.

### Comparação fora da classe
Funções de comparação para os candidatos baseadas nos seguintes critérios:

- Alfabética pelo nome em ordem crescente
- Alfabética pelo nome em ordem decrescente
- Pelo total dos bens (crescente e decrescente)
- Pelo partido e nome (alfabética, crescente e decrescente)
- Pela data de nascimento (crescente e decrescente)

## Classe Controle()
> Classe principal do programa

Deve conter as seguintes funcionalidades:

- [x] **1. Carregar candidatos:** Carregamento dos candidatos a partir do arquivo (o caminho do arquivo deve ser um parâmetro do método).
Os candidatos lidos do arquivo deverão ser armazenados em objetos do tipo ```Candidato``` e inseridos numa lista de candidatos;
- [x] **2. Carregar bens:** Carregamento dos bens dos candidatos. Os bens deverão ser lidos do arquivo cujo caminho é passado como
parâmetro para o método. Cada bem lido deverá ser armazenado em um objeto do tipo ```Bem``` e inserido na lista de bens de seu respectivo
candidato. A correspondência deve ser feita pelo ID do candidato;
- [x] **3. Recuperar lista de candidatos:** Deve-se implementar funções/métodos que recuperem a lista de candidatos de um determinado
partido, UF, nascidos em um dado município, candidatos a um determinado cargo, cujo total de bens declarados esteja acima de um valor
especificado pelo usuário, ou que tenham ou não sido eleitos no pleito;
- [x] **4. Exibir lista:** Deve-se implementar uma função/método que permita exibir a lista obtida no item 3;
- [x] **5. Média dos bens:** Funções que mostram a média do total de bens dos candidatos por cargo, UF, partido, ocupação, ou ano de
nascimento;
- [x] **6. Remover da Lista:** Função que remove da lista todos os candidatos que satisfaçam um critério.
   > Exemplo: remover todos os candidatos com a candidatura indeferida, ou que não tenham sido eleitos.
