# Lista 01 - Programação Orientada à Objetos

<p align='justify'>
  Q1. Escreva em Python uma classe Cronometro, que seja capaz de cronometrar o tempo passado no sistema a partir de dois métodos (iniciar e parar). Para isso você pode importar a biblioteca time e usar o método time.clock() para obter o tempo atual do sistema. A  classe Cronometro deve implementar os seguintes métodos:
</p>

<table> 
  <tr>
    <td> Construtor </td>
    <td>Método construtor padrão de qualquer objeto </td>
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
    <td> Exibe o tempo contado pelo cronômetro </td>
  </tr>
</table>
<br>
<p align='justify'>
  Q2. Você deve ter notado que ao tentar imprimir ou exibir o seu objeto do tipo Cronômetro, é exibido na tela algo como isso ‘<__main__.Cronometro at 0x1954ce16ba8>’. Isso acontece por sua classe ainda não possuir um método de exibição válido, por tanto são exibidas as informações do arquivo de script que contém a implementação do objeto (sendo __main__ o script principal que o console está
executando, caso contrário será exibido o nome do arquivo de script do qual a classe foi importada), seguido pelo nome da classe e o endereço físico de memória no qual o objeto está salvo. Os métodos que controlam a exibição válida de um objeto são os métodos mágicos __str__ e __repr__. O método __str__ controla a exibição do objeto quando é chamada a função print ou quando ele é convertido diretamente para string. O método __repr__ controla a exibição válida (reprodução) do objeto. Representando uma forma de inicializar um objeto de valor igual, ou seja, você deve ser capaz de instanciar o objeto de valor igual ao original. Escreva os métodos __str__ e __repr__ da seguinte forma:
</p>

<table>
  <tr>
    <td> __str__ </td>
    <td> Exibe apenas a quantidade de segundos que se passaram desde o início (método iniciar) da contagem </td>
  </tr>
  <tr>
    <td> __repr__ </td>
    <td> Representação válida do objeto. Capaz de ser instanciado.</td>
  </tr>
</table>
