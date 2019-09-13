# Lista 01 - Programação Orientada à Objetos

<ol>
    <li>Escreva em Python uma classe Cronometro, que seja capaz de cronometrar o tempo passado no sistema a partir de dois métodos (iniciar e parar). Para isso você pode importar a biblioteca time e usar o método time.clock() para obter o tempo atual do sistema. A classe Cronometro deve implementar os seguintes métodos:
        <br><br>
        <table>
            <tr>
                <td> Construtor </td>
                <td> Método construtor padrão de qualquer objeto </td>
            </tr>
            <tr>
                <td> Iniciar </td>
                <td> Inicia a contagem do tempo do relógio </td>
            </tr>
            <tr>
                <td> Parar </td>
                <td> Para a contagem do tempo do relógio </td>
            </tr>
            <tr>
                <td> Zerar </td>
                <td> Zera o contador </td>
            </tr>
            <tr>
                <td> Exibir </td>
                <td> Exibe o tempo contado pelo cronômetro  </td>
            </tr>
        </table>
    </li>
    <br>
    <li> Você deve ter notado que ao tentar imprimir ou exibir o seu objeto do tipo Cronômetro, é exibido na tela algo como isso ‘<__main__.Cronometro at 0x1954ce16ba8>’. Isso acontece por sua classe ainda não possuir um método de exibição válido, por tanto são exibidas as informações do arquivo de script que contém a implementação do objeto (sendo __main__ o script principal que o console está executando, caso contrário será exibido o nome do arquivo de script do qual a classe foi importada), seguido pelo nome da classe e o endereço físico de memória no qual o objeto está salvo. Os métodos que controlam a exibição válida de um objeto são os métodos mágicos __str__ e __repr__. O método __str__ controla a exibição do objeto quando é chamada a função print ou quando ele é convertido diretamente para string. O método __repr__ controla a exibição válida (reprodução) do objeto. Representando uma forma de inicializar um objeto de valor igual, ou seja, você deve ser capaz de instanciar o objeto de valor igual ao original. Escreva os métodos __str__ e __repr__ da seguinte forma: 
        <br><br>
        <table>
            <tr>
                <td> __str__ </td>
                <td> Exibe apenas a quantidade de segundos que se passaram desde o início (método iniciar) da contagem</td>
            </tr>
            <tr>
                <td> __repr__ </td>
                <td> Representação válida do objeto. Capaz de ser instanciado.</td>
            </tr>
        </table>
    </li>
    <br>
    <li> Um outro ponto importante da programação orientada a objetos é o encapsulamento de atributos e métodos dos objetos. Em Python, é possível tornar um atributo semi-privado apenas adicionando um underline (_) antes do nome do objeto. Apesar de tornar o atributo semi-privado, ainda é possível acessar o atributo normalmente utilizando o nome da instância, seguido de . e do nome do método com um underline na frente. No entanto, é possível tornar atributos privados com a adição de dois underlines na frente do nome do atributo. Fazendo isso, você torna o atributo privado e inacessível de forma normal, como por exemplo usando o nome do atributo precedido de dois underlines. Em Python, no entanto é possível acessar atributos e métodos privados usando a seguinte expressão: 
        <br><br>
        nome_da_instancia._nome_do_objeto__nome_do_atributo
        <br><br>
        Imagine que o atributo tempo da classe Cronometro é um atributo privado, e imagina que eu tenha criado uma instância de objeto Cronometro com o nome relogio. Acessar o atributo tempo da seguinte forma:
        <br><br>
        relogio._Cronometro__tempo
        <br><br>
        Tendo isso em mente, modifique a sua classe Cronometro para ter todos os atributos privados e crie métodos ‘getters’ para acessar esses atributos.
    </li>
    <br>
    <li>Para a questão 4, você deve usar a classe Cronometro implementada nas questões 1 e 2 para resolver o problema proposto. Deverá ser implementada uma função que conta quantas triplas em um vetor de inteiros somam a zero (número de elementos distintos de um vetor que, quando somados, resultam em zero). Essa implementação deverá ser realizada no protótipo disponibilizado.
    </li>
</ol>
