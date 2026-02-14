# A pesquisa binária é executada com tempo logarítmico. 
def busca_binaria(vetor, alvo):
    inicio = 0
    fim = len(vetor) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        if vetor[meio] == alvo:
            return meio  # índice encontrado
        elif vetor[meio] < alvo:
            inicio = meio + 1  # procura na metade direita
        else:
            fim = meio - 1  # procura na metade esquerda
    return -1  # não encontrado


vetor = [12, 25, 33, 37, 48, 57, 86, 92]
alvo = 37

resultado = busca_binaria(vetor, alvo)
if resultado != -1:
    print(f"Elemento {alvo} encontrado na posição {resultado}.")
else:
    print(f"Elemento {alvo} não encontrado.")
