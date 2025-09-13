def selecao_crescente(lis):
    tamanho_lista = len(lis)  # Obtém o tamanho da lista

    # Loop externo: percorre cada posição da lista, exceto a última
    for p in range(tamanho_lista - 1):
        # Começamos assumindo que o menor valor está na posição atual (p)
        indice_menor = p

        # Loop interno: percorre o restante da lista, a partir de p+1
        for i in range(p + 1, tamanho_lista):
            # Se encontrarmos um valor menor do que o atual menor, atualizamos o índice
            if lis[i] < lis[indice_menor]:
                indice_menor = i

        # Se o menor valor não estiver na posição correta, fazemos a troca
        if indice_menor != p:
            lis[p], lis[indice_menor] = lis[indice_menor], lis[p]

    return lis  # Retorna a lista ordenada