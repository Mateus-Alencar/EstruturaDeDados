class Pilha2:
    def __init__(self):
        self.itens = []

    def is_vazia(self):
        # Verifica se a Pilha está vazia
        return len(self.itens) == 0

    def enfileirar(self, item):
        # Adiciona um item no final da Pilha (***PUSH***)
        self.itens.append(item)
        print(f'Item {item} enfileirado. Fila: {self.itens}')

    def desenfileirar(self):
        # Remove o item da frente da Pilha (primeiro item) (***POP***)
        if self.is_vazia():
            print("A fila está vazia. Não é possível desenfileirar.")
            return None
        else:
            # O método pop(0) remove o primeiro item da Pilha (frente da fila)
            item = self.itens.pop(0)
            print(f'Item {item} desenfileirado. Fila: {self.itens}')
            return item

    def frente(self):
        # Retorna o item da frente da Pilha sem removê-lo
        if self.is_vazia():
            print("A Pilha está vazia. Não há frente.")
            return None
        return self.itens[0]  # O primeiro item da lista é o item da frente da Pilha

    def tamanho(self):
        contador = 0
        aux = []
    
        # Desenfileira os itens para contar e os coloca na Pilha auxiliar
        while not self.is_vazia():
            item = self.desenfileirar()
            aux.append(item)  
            contador += 1  
            
        # Restaura os itens para a Pilha original
        while aux:
            item = aux.pop(0)  
            self.enfileirar(item)  
    
        return contador


    def imprimir_Pilha(self):
        # Imprime os elementos da Pilha
        if self.is_vazia():
            print("A Pilha está vazia.")
        else:
            print(f'Pilha: {self.itens}')

# Exemplo de uso da fila
Pilha = Pilha2()

Pilha.enfileirar(10)  
Pilha.enfileirar(20) 
Pilha.enfileirar(30)  
Pilha.enfileirar(40)  
Pilha.enfileirar(80)  
Pilha.enfileirar(70)  

# Ver a frente da fila
print(f'Frente da fila: {Pilha.frente()}')

# Desenfileirar um item
Pilha.desenfileirar()  # Remove o item da frente (10)

# Imprimir o estado atual da fila
Pilha.imprimir_Pilha()

# Verificar o tamanho da fila
print(f'Tamanho da fila: {Pilha.tamanho()}')

# Desenfileirar todos os itens
Pilha.desenfileirar()  # Remove 20
Pilha.desenfileirar()  # Remove 30
Pilha.desenfileirar()  # Tenta remover de uma fila vazia

# Verificar o tamanho da fila
print(f'Tamanho da fila: {Pilha.tamanho()}')

# Imprimir o estado da fila novamente
Pilha.imprimir_Pilha()

Pilha.desenfileirar()
Pilha.desenfileirar()

Pilha.imprimir_Pilha()

# Verificar o tamanho da fila
print(f'Tamanho da fila: {Pilha.tamanho()}')
