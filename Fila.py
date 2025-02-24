class Fila:
    def __init__(self):
        self.itens = []

    def is_vazia(self):
        # Verifica se a fila está vazia
        return len(self.itens) == 0

    def enfileirar(self, item):
        # Adiciona um item no final da fila
        self.itens.append(item)
        print(f'Item {item} enfileirado. Fila: {self.itens}')

    def desenfileirar(self):
        # Remove o item da frente da fila (primeiro item)
        if self.is_vazia():
            print("A fila está vazia. Não é possível desenfileirar.")
            return None
        else:
            # O método pop(0) remove o primeiro item da lista (frente da fila)
            item = self.itens.pop(0)
            print(f'Item {item} desenfileirado. Fila: {self.itens}')
            return item

    def frente(self):
        # Retorna o item da frente da fila sem removê-lo
        if self.is_vazia():
            print("A fila está vazia. Não há frente.")
            return None
        return self.itens[0]  # O primeiro item da lista é o item da frente da fila

    def tamanho(self):
        # Retorna o número de itens na fila
        return len(self.itens)

    def imprimir_fila(self):
        # Imprime os elementos da fila
        if self.is_vazia():
            print("A fila está vazia.")
        else:
            print(f'Fila: {self.itens}')

# Exemplo de uso da fila
fila = Fila()

fila.enfileirar(10)  
fila.enfileirar(20) 
fila.enfileirar(30)  
fila.enfileirar(40)  
fila.enfileirar(80)  
fila.enfileirar(70)  

# Ver a frente da fila
print(f'Frente da fila: {fila.frente()}')

# Desenfileirar um item
fila.desenfileirar()  # Remove o item da frente (10)

# Imprimir o estado atual da fila
fila.imprimir_fila()

# Verificar o tamanho da fila
print(f'Tamanho da fila: {fila.tamanho()}')

# Desenfileirar todos os itens
fila.desenfileirar()  # Remove 20
fila.desenfileirar()  # Remove 30
fila.desenfileirar()  # Tenta remover de uma fila vazia

# Imprimir o estado da fila novamente
fila.imprimir_fila()

fila.desenfileirar()
fila.desenfileirar()

fila.imprimir_fila()
