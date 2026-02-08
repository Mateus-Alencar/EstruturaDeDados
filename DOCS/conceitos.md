# Estruturas de Dados

## Pesquisa binária
A pesquisa binária é um algoritmo. Sua entrada é uma lista ordenada de elementos. Se o elemento que você está buscando está na lista, a pesquisa binária retorna a sua localização. 

A pesquisa binária é executada com tempo logarítmico, por exemplo, se a lista tem 100 itens, precisa-se de, no máximo, sete tentativas. Se tem 4 bilhões, precisa-se de, no máximo, 32 tentativas.  

[Exemplo de código](../Python/Método_de_Pesquisa/busca_binaria.py)

## Ordenação por seleção
A ordenação por seleção (Selection Sort) funciona escolhendo repetidamente o menor elemento e colocando-o na posição correta.

A ordenação por seleção percorre o vetor várias vezes e, a cada passo:
1. Encontra o menor elemento da parte não ordenada
2. Troca esse elemento com a posição atual
3.  Avança para a próxima posição

*Esse processo se repete até que todo o vetor esteja ordenado.*

[Exemplo de código](../Python/Metodo_selecao/ordenacao_selecao.py)

**Estruturas relacionadas**
>[!WARNING]
> - No array, todos os elementos são armazenados um ao lado do outro.
> - Na lista, os elementos estão espalhados e um elemento armazena o
endereço do próximo elemento.

>[!NOTE]
> - Arrays permitem leituras rápidas.
> - Listas encadeadas permitem rápidas inserções e eliminações.
