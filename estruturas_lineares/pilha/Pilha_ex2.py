class Pilha2:
    def __init__(self):
        self.itens = []

    def is_vazia(self):
        return len(self.itens) == 0

    def enfileirar(self, item):
        self.itens.append(item)
        print(f'Item {item} enfileirado. Fila: {self.itens}')

    def desenfileirar(self):
        if self.is_vazia():
            print("A fila está vazia. Não é possível desenfileirar.")
            return None
        else:
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
        if self.is_vazia():
            print("A Pilha está vazia.")
        else:
            print(f'Pilha: {self.itens}')

Pilha = Pilha2()

Pilha.enfileirar(10)  
Pilha.enfileirar(20) 
Pilha.enfileirar(30)  
Pilha.enfileirar(40)  
Pilha.enfileirar(80)  
Pilha.enfileirar(70)  

print(f'Frente da fila: {Pilha.frente()}')

Pilha.desenfileirar()

Pilha.imprimir_Pilha()

print(f'Tamanho da fila: {Pilha.tamanho()}')

Pilha.desenfileirar()
Pilha.desenfileirar()
Pilha.desenfileirar()

print(f'Tamanho da fila: {Pilha.tamanho()}')

Pilha.imprimir_Pilha()

Pilha.desenfileirar()
Pilha.desenfileirar()

Pilha.imprimir_Pilha()

print(f'Tamanho da fila: {Pilha.tamanho()}')
