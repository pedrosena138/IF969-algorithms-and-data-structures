# Exercício de Sala 01 - Programação Orientada à Objetos

**1. Faça um sistema de notas da sua sala:**  
**a.** Crie uma classe Aluno que possui 3 notas. Ao inicializar a classe, passe como parâmetro o CPF e o nome do aluno;  
**b.** A classe possui 3 métodos:  
* ```inicializarNota(nota,numeroProva)```: tem como parâmetros a nota e o número (1,2,3) da nota a ser inicializada;  
* ```verificaSituacaoMedia()```: que não possui parâmetros e retorna True se o aluno tem média acima de 7 e False caso contrário. Se as 3 notas não foram inicializadas, imprima uma mensagem na tela e retorne False;    
* ```imprimeInformacoes()```: que não possui parâmetros e imprime o nome, CPF e as 3 notas do aluno. Se alguma das notas não foi fornecida, imprima "nota x não fornecida".  

**2. Faça um sistema de compras:**  
**a.** Crie uma **classe abstrata** _Empreendimento_ que possui os métodos abstratos ```getNome()```, ```setNome()```, ```getCNPJ()```, ```setCNPJ(novoCNPJ)```, ```getEndereco()```, ```setEndereco(novoEndereco)```, ```getSaldo()```, ```setVenda(venda)```;  
**b.** Crie uma **subclasse** _Supermercado_ que herda da classe _Empreedimento_ e implementa os métodos ```__init__()```, ```getNome()```, ```setNome(nome)```, ```getCNPJ()```, ```setCNPJ(novoCNPJ)```, ```getSaldo()```, ```setVenda(venda)```. Ao inicializar um objeto dessa classe, deve-se passar o nome, CNPJ e endereço como parâmetros;  
**c.** O método ```getSaldo()``` retorna o valor do atributo encapsulado _saldo_. O método ```setVenda(venda)``` atualiza o valor do atributo encapsulado _saldo_ somando-o com um atributo fornecido como parâmetro;  
**d.** Inicialize 3 objetos do tipo _Supermercado_: _VarejaoCIn_, _CompraUFPE_ e _EstudantesVarzea_. Peça para o usuário fornecer as informações iniciais e depois pergunte se houve alguma venda para cada um dos supermercados. Encerre imprimindo as informações gerais dos supermercados.  

**3. Crie uma classe Programa:**  
**a.** Atributos: ```anoCriacao```, ```codigo```, ```nomeDono```, ```emailDono```, ```numeroLinhas```;  
**b.** Metodos: 
* _getX_ e _setX_ para cada um dos X atributos;  
* ```calculaNumeroLinhas```: acessa o código do Programa, conta a quantidade de linhas desse código e atualiza o atributo ```numeroLinhas```;  
* ```calculaIdadeCodigo(anoAtual)```: acessa o ano de criação do código e verifica a idade do código de acordo com o parâmetro ```anoAtual``` fornecido como parâmetro;  
**c.** Crie um método fora da classe: ```comparaCodigo(programa1,programa2)``` que recebe dois objetos do tipo Programa como parâmetros e compara os códigos retornando verdadeiro se eles forem iguais.
