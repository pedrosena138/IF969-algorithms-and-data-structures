# Exercício de Sala 01 - Programação Orientada à Objetos
<dl>
    <dt>1. Faça um sistema de notas da sua sala:</dt>
        <dd>
            <strong>a.</strong> Crie uma classe Aluno que possui 3 notas. Ao inicializar a classe, passe como parâmetro o CPF e o nome do aluno.
        </dd>
        <dd>
            <strong>b.</strong> A classe possui 3 métodos: <strong>inicializarNota(nota,numeroProva)</strong> que tem como parâmetros a nota e o número (1,2,3) da nota a ser inicializada; <strong>verificaSituacaoMedia()</strong>, que não possui parâmetros e retorna True se o aluno tem média acima de 7 e False caso contrário. Se as 3 notas não foram inicializadas, imprima uma mensagem na tela e retorne False; <strong>imprimeInformacoes()</strong>, que não possui parâmetros e imprime o nome, CPF e as 3 notas do aluno. Se alguma das notas não foi fornecida, imprima "nota x não fornecida".
        </dd>
    <dt>2. Faça um sistema de compras:</dt>
        <dd>
            <strong>a.</strong> Crie uma <strong>classe abstrata</strong> <u>Empreendimento</u> que possui os métodos abstratos getNome, setNome, getCNPJ, setCNPJ, getEndereco, setEndereco, getSaldo, setVenda.
        </dd>
        <dd>
            <strong>b.</strong> Crie uma<strong>subclasse</strong> <u>Supermercado</u> que herda da classe Empreedimento e implementa os métodos <strong>__init__, getNome, setNome, getCNPJ, setCNPJ, getSaldo, setVenda</strong>. Ao inicializar um objeto dessa classe, deve-se passar o nome, CNPJ e endereço como parâmetros.
        </dd>
        <dd>
            <strong>c.</strong> O método <strong>getSaldo</strong> retorna o valor do atributo encapsulado <i>saldo</i>. O método <strong>setVenda</strong> atualiza o valor do atributo encapsulado <i>saldo</i> somando-o com um atributo fornecido como parâmetro.
        </dd>
        <dd>
            <strong>d.</strong> Inicialize 3 objetos do tipo Supermercado: VarejaoCIn, CompraUFPE e EstudantesVarzea. Peça para o usuário fornecer as informações iniciais e depois pergunte se houve alguma venda para cada um dos supermercados. Encerre imprimindo as informações gerais dos supermercados.
        </dd>
    <dt>3. Crie uma classe Programa:</dt>
        <dd>
            <strong>a.</strong> Atributos: anoCriacao (int), codigo (string), nomeDono(string),       emailDono(string), numeroLinhas(inteiro).           
        </dd>
        <dd>
            <strong>b.</strong> Metodos: <strong>getX</strong> e <strong>setX</strong> para cada um dos X atributos <strong>calculaNumeroLinhas</strong> (acessa o código do Programa, conta a quantidade de linhas desse código e atualiza o atributo <strong>numeroLinhas</strong>);              <strong>calculaIdadeCodigo(anoAtual)</strong> (acessa o ano de criação do código e verifica a idade do código de acordo com o parâmetro <strong>anoAtual</strong> fornecido como parâmetro). 
        </dd>
        <dd>
            <strong>c.</strong> Crie um método fora da classe: <strong>comparaCodigo(programa1,programa2)</strong> que recebe dois objetos do tipo Programa como parâmetros e compara os códigos retornando verdadeiro se eles forem iguais.
        </dd>
</dl>
