# Lista 01 - Programação Orientada à Objetos

**1. Escreva em Python uma classe _Cronometro_, que seja capaz de cronometrar o tempo passado no sistema a partir de dois métodos (iniciar e parar). Para isso você pode importar a biblioteca ```time``` e usar o ~~método ```time.clock()```~~(depreciado) para obter o tempo atual do sistema. A classe Cronometro deve implementar os seguintes métodos:**  
> Ao invés do método ```time.clock()```, utilize o método ```perf_counter()```

|   Método   | Descrição                                   |
|------------|---------------------------------------------|
| Construtor | Método construtor padrão de qualquer objeto |    
| Iniciar    | Inicia a contagem do tempo do relógio       |
| Parar      | Para a contagem do tempo do relógio         |
| Zerar      | Zera o contador                             |
| Exibir     | Exibe o tempo contado pelo cronômetro       |


**2. Escreva os métodos** ```__str__``` **e** ```__repr__``` **da seguinte forma:**   

|   Método       | Descrição                                   |
|----------------|---------------------------------------------------------------------------------------------------|
| ```__str__```  | Exibe apenas a quantidade de segundos que se passaram desde o início (método iniciar) da contagem |    
| ```__repr__``` | Representação válida do objeto. Capaz de ser instanciado                                          |


**3. Modifique a sua classe _Cronometro_ para ter todos os atributos privados e crie métodos ‘getters’ para acessar esses atributos.** Em Python para deixar os atributos e métodos 'privados' adicionando dois underlines na frente (```__atributo```**,** ```__metodo()```), porém não ficam totalmente privados, ainda é possível acessá-los utilizando a seguinte sintaxe(```instancia.objeto__atributo``` ou ```instancia.objeto__metodo()```). Pois, segundo o paradigma da linguagem:
> We are all consenting adults here. (Somos todos adultos com consentimento aqui.)

**4. Você deve usar a classe Cronometro implementada nas questões 1 e 2 para resolver o problema proposto. Deverá ser implementada uma função que conta quantas triplas em um vetor de inteiros somam a zero (número de elementos distintos de um vetor que, quando somados, resultam em zero). Essa implementação deverá ser realizada no protótipo disponibilizado. Deverá também testar e armazenar os resultados da execução do programa implementado. Após coletar os dados para os diversos experimentos, você deverá plotar os resultados para identificar o comportamento dos algoritmos. Você deverá também encontrar a curva que melhor se ajusta aos pontos usando regressão linear. Essa técnica já está implementada em diversas ferramentas, inclusive no Excel (procure por adicionar linha de tendência).**
