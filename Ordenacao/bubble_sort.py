# Utilizando o vetor: 25, 57, 48, 37, 12, 92, 86, 33. Faça a ordenação em ordem crescente utilizando o método de Bubble sort

def bubble_sort(vetor):
    n = len(vetor)
    for i in range(n - 1):           
        for j in range(n - i - 1):   
            if vetor[j] > vetor[j + 1]: 
                vetor[j], vetor[j + 1] = vetor[j + 1], vetor[j]  
    return vetor

vetor = [25, 57, 48, 37, 12, 92, 86, 33]
print("Vetor ordenado:", bubble_sort(vetor))

# Cada passagem consiste em comparar cada elemento no arquivo com seu sucessor (x[i] 
# com x[i + 1]) e trocar os dois elementos se eles não estiverem na ordem correta.
