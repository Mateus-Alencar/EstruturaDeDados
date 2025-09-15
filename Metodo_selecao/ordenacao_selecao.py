# 1) Escreva uma versão do método de seleção para continuar com o processo
# de ordenação apenas se o conjunto não estiver ordenado.

def selecao_ordenada (lis):
    tamanho_lista = len(lis)
    ordenada=True
    for posicao in range(tamanho_lista-1):
        for i in range(tamanho_lista-1):
            if lis[i]>lis[i+1]:
                ordenada = False
                break
        if ordenada:
            return lis
        indice_menor=posicao
        for indice in range(posicao+1, tamanho_lista):
            if lis[indice]<lis[posicao]:
                indice_menor=indice
        if indice_menor != posicao:
            lis[posicao], lis[indice_menor] = lis[indice_menor], lis[posicao]
    return lis

print(selecao_ordenada([3,2,1,4,5,6,0,7,8,9,10]))
# 2) Escreva uma versão do método de ordenação por seleção para receber
# a quantidade de comparações e de trocas realizadas durante a ordenação.

def selecao_ordenada_contador(lis):
    tamanho_lista = len(lis)
    comparacoes = 0  # Contador de comparações
    trocas = 0       # Contador de trocas

    for posicao in range(tamanho_lista-1):
        indice_menor = posicao
        for indice in range(posicao+1, tamanho_lista):
            comparacoes += 1  # Contabiliza cada comparação
            if lis[indice] < lis[indice_menor]:
                indice_menor = indice
        if indice_menor != posicao:
            trocas += 1
            lis[posicao], lis[indice_menor] = lis[indice_menor], lis[posicao]

    print("Trocas:", trocas)
    print("Comparações:", comparacoes)
    return lis

print(selecao_ordenada_contador([3,2,1,4,5,6,0,7,8,9,10]))

