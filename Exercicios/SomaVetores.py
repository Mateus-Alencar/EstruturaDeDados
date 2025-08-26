# Função recursiva responsável por retornar a soma dos elementos de um vetor.
def somaVetor(vetor, numElem):
    if numElem == 0:
        return 0
    else:
        return somaVetor(vetor,numElem-1) + vetor[numElem-1]

def somaVetorNumPositivos(vetor, numElem):
    if numElem == 0:
        return 0
    else:
        if vetor[numElem-1] > 0:
            return somaVetorNumPositivos(vetor,numElem-1) + vetor[numElem-1]
        else:
            return somaVetorNumPositivos(vetor, numElem-1)
            
def encontrarMaiorElementoVetor(vetor, numElem):
    if numElem == 1:
        return vetor[0]
    else:
        valor = encontrarMaiorElementoVetor(vetor, numElem-1)
        if valor > vetor[numElem-1]:
            return valor
        else: 
            return vetor[numElem-1]


def encontrarPosicaoMaiorValorVetor(vetor, numElem):
    if numElem == 1:
        return vetor[0]
    else:
        valor = encontrarPosicaoMaiorValorVetor(vetor, numElem-1)
        if valor<vetor[numElem-1]:
            return numElem
        else: 
            return numElem-1
print(encontrarPosicaoMaiorValorVetor([1,2,3,-4], 4))
