# EstruturaDeDados

A estrutura de dados é uma maneira de organizar e armazenar dados para que possam ser usados de forma eficiente. Ela define a forma como os dados são armazenados, acessados e manipulados dentro de um programa ou sistema.

As principais estruturas de dados incluem:

## Vetores (Arrays):
- Armazenam elementos de maneira sequencial e contínua na memória.
- Acesso rápido aos elementos, mas o tamanho é fixo.

## Listas:
- Sequência de elementos onde cada elemento aponta para o próximo.
- Listas podem ser simples (apenas com um ponteiro para o próximo) ou duplamente encadeadas (com ponteiro para o próximo e para o anterior).

## Pilhas (Stacks):
- Funciona no princípio "Último a Entrar, Primeiro a Sair" (LIFO).
- Ideal para situações como desfazer ações ou chamadas de funções.

## Filas (Queues):
- Funciona no princípio "Primeiro a Entrar, Primeiro a Sair" (FIFO).
- Usada para controle de tarefas em que a ordem de chegada importa (como em sistemas de impressão).

## Filas Encadeadas:
- Uma fila encadeada é uma variação da estrutura de fila, onde os elementos são armazenados em **nós** (objetos), e cada nó contém o valor e uma referência (ponteiro) para o próximo nó.
- Ao contrário das filas tradicionais que usam um array ou lista para armazenar os elementos de forma sequencial, as filas encadeadas não têm um tamanho fixo, o que permite a inserção e remoção de elementos sem a necessidade de realocar toda a estrutura.
- A inserção de novos elementos acontece sempre no **final** da fila (enfileiramento), enquanto a remoção ocorre sempre na **frente** da fila (desenfileiramento), mantendo o princípio FIFO.
- O **primeiro** nó da fila é chamado de **frente**, e o **último** nó é chamado de **final**.

## Árvores:
- Estruturas hierárquicas, com um nó raiz e nós filhos.
- Utilizadas para representar hierarquias (como pastas de arquivos ou estruturas de diretórios).

## Tabelas Hash (Hash Tables):
- Usadas para associar chaves a valores.
- Permitem buscas rápidas, inserções e exclusões.

## Grafos:
- Representam relações entre elementos de forma não hierárquica.
- São compostos por vértices (nós) e arestas (ligações entre vértices).
