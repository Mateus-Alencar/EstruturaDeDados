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
            
print(somaVetor([1,2,3,4], 4))
