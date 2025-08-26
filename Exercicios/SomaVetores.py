# Função recursiva responsável por retornar a soma dos elementos de um vetor.
def somaVetor(vetor, numElem):
    if numElem == 0:
        return 0
    else:
        return somaVetor(vetor,numElem-1) + vetor[numElem-1]

    
print(somaVetor([1,2,3,4], 4))
