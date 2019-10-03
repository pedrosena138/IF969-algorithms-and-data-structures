# Lista 03 - Árvores
**1. Implemente a classe árvore binária, assim como seus métodos especiais e particularidades de acordo com as diretrizes a seguir:**
- ```__bool__```: Esse método converte a estrutura em um valor booleano;
- ```__str__```: deve imprimir os elementos da árvore do caminhamento em ordem;
- ```__repr__```: deve ser capaz de inicializar uma instância de árvore de igual valor e, por tanto, deve dispor os elementos impressos em pré-ordem;
- ```__iter__```: também deve iterar pela árvore em pré-ordem;
- ```__delitem__```: Além dos métodos ```__getitem__``` e ```__setitem__```, teremos na nossa árvore binária o
método ```__delitem__```. Esse método é responśavel pelo comportamento da estrutura quando uma expresão do tipo ```del arvore[0]``` é chamada;
- ```__contains__```: Com este método, dado uma chave, o método retorna ```True``` ou ```False``` para determinar se a chave está contida na árvore. Esse é o método responsável pelo comportamento de comandos como ```chave’ in arvore```.

**2. Usando o conceito de herança, implemente a classe AVL como herança direta da sua árvore binária. Assim como para árvore binária há algumas restrições e cuidados a serem tomados na implementação da AVL:**
- Implemente um método estático ```balanceada``` que recebe como parâmetro uma árvore binária e retorna ```True``` ou ```False``` dependendo do nível de balanceamento da árvore;
- Implemente um outro método estático ```balancear``` que receba como parâmetro uma árvore binária e faça o balanceamento da árvore existente. Esse método não deve retornar uma nova árvore, mas sim balancear o objeto passado como parâmetro e, por tanto não deve possuir retorno;
- Implemente o método ```coef_balanceamento```, este deve receber como parâmetro uma subárvore e retornar o coeficiente de balanceamento desta. Implemente o método de forma recursiva;
- Implemente os métodos ```girar_esquerda``` e ```girar_direita```;
- Por fim faça a sobrescreva os métodos de inserção e remoção para que sua AVL se mantenha balanceada.

A classe ```No``` deve ter a seguinte implementação:
- A classe nó deve guardar um par chave-valor, sendo assim indexada pela chave. Embora normalmente qualquer objeto possa ser usado para indexar um nó, na nossa implementação de árvore binária considere que as chaves serão sempre do tipo string.
- Implemente os métodos comparativos:

| Método       | Função |
|--------------|--------|
| ```__lt__``` | <      |    
| ```__gt__``` | >      |
| ```__le__``` | <=     |
| ```__ge__``` | >=     |
| ```__eq__``` | ==     |
| ```__ne__``` | !=     |
