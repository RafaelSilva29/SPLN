# Trabalho Prático 1

# Resumo
Neste trabalho prático foi criada uma script para receber um ficheiro de texto como input.
Esta script encontra nomes de personagens no texto e guarda a ocorrência de vários nomes na mesma frase, com o objetivo de criar pares de nomes que vão ocorrendo juntos. Assim podemos criar um grafo com as relações das personagens e obter um estudo sobre as personagens de um livro, como por exemplo, qual a personagem com mais amigos, quais os seus melhores amigos, etc...

# Funções
**frases** => encontrar o inicio das frases e marcá-las com @

**marcarNomes** => encontra os nomes no texto, ou seja, todas as palavras começadas com letra maiuscula, mas excluindo os inicios das frases. Marca estes nomes com parêntesis.

**getNomes** => lê novamente o texto com as palavras marcadas, e cria um set com todos os nomes existentes no texto.

**getPares** => já tendo os nomes das personagens, voltamos a ler o texto e registamos todos os pares de nomes que aparecem juntos na mesma frase. De referir que registamos todas as combinações possiveis de pares. No final da execução desta função já temos uma lista com todos os pares existentes e o número de ocorrências respetivo.

**otimiza** => esta função aplica um filtro aos pares existentes de forma a tentar remover desta lista os pares pouco relevantes ou possiveis palavras que tenham sido apanhadas que não fossem nomes. Para isto, fizemos um levantamento das palavras que foram apanhadas e não são relevantes e juntamos numa lista. Com a aplicação desta função removemos todos os pares que continham estas palavras e mantemos apenas os pares com mais 5 ou mais ocorrências.

**numeroAmigos** => através de o grafo criado com as relações, dada uma personagem, esta função devolve o seu número de amigos.

**topAmigos** => dada uma personagem, esta função cria uma lista com os amigos da persongam, ordenada por ordem decrescente de proximidade.

**showGrafoIndividual** => dado um grafo e uma persongam, efetua um plot para mostrar ao utilizador o grafo com as relações da persongam escolhida.

# Execução
1. Executamos a função otimiza para obter os pares de relações das personagens e o grau de proximidade (dado pela quantidade de vezes que o par aparece junto).

2. Construimos o grafo através da lista de pares obtida anteriormente.

3. Efetuamos o plot do grafo, para mostrar ao utilizador o grafo com todas as relações existentes.

4. Executamos o interpretador, que espera que o utilizador indique o nome de uma personagem e lhe devolve o seu número de amigos, a lista dos 5 amigos mais próximos e por fim mostra o grafo que contém apenas as relações da personagem indicada. De seguida poderá continuar a indicar outras personagens.
