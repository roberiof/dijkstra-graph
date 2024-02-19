# Dijkstra - Blogs Políticos

Contexto do problema:

Para entender melhor o algoritmo de Dijkstra, decidimos aplicá-lo a um cenário prático. Utilizamos um conjunto de dados relacionado às Eleições americanas de 2004, representado como uma rede de blogs. Cada nó neste conjunto de dados representa um blog, e as arestas entre os nós indicam citações de um blog para outro. No entanto, o conjunto de dados não continha pesos nas arestas, então adicionamos pesos manualmente para poder testar o algoritmo de Dijkstra.
Implementação:

Algoritmo Utilizado:
O algoritmo utilizado é o de Dijkstra, uma técnica de caminho mínimo que encontra o caminho mais curto entre dois nós em um grafo ponderado, neste caso, representando a rede de blogs.

Desenvolvimento:
Leitura do conjunto de dados em formato GML usando NetworkX.
Construção do grafo com pesos aleatórios para as arestas.
Utilização do algoritmo de Dijkstra para encontrar o caminho mais curto entre dois blogs especificados pelo usuário.

Bibliotecas Utilizadas:
NetworkX: Para trabalhar com grafos.
Random: Para gerar pesos aleatórios para as arestas.

Conclusão:
O programa solicita ao usuário que escolha dois blogs para encontrar o caminho mais curto entre eles. Em seguida, aplicamos o algoritmo de Dijkstra ao grafo ponderado dos blogs, encontrando o caminho com a menor soma de pesos entre nós. Finalmente, exibe o caminho encontrado e a soma dos pesos.



Isso demonstra que o programa é capaz de encontrar o caminho mais curto entre dois blogs na rede, considerando os pesos adicionados manualmente às arestas.


Referências:
Skewed Data - Networks. Polblogs. Disponível em: <https://networks.skewed.de/net/polblogs>. Acesso em: [18/01/2024].

<br/>

Os pesos foram colocados aleatoriamente.
