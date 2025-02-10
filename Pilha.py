class Pilha:
    def __init__(self):
        # A pilha será representada por uma lista interna
        # Inicialmente a pilha está vazia
        self.itens = []

    def is_vazia(self):
        # Retorna True se a pilha estiver vazia, caso contrário retorna False
        return len(self.itens) == 0

    def empilhar(self, item):
        # Adiciona um item no topo da pilha
        # A operação de empilhar é realizada com o método append() da lista
        self.itens.append(item)
        print(f'Item {item} empilhado. Pilha: {self.itens}')

    def desempilhar(self):
        # Remove o item do topo da pilha
        if self.is_vazia():
            print("A pilha está vazia. Não é possível desempilhar.")
            return None
        else:
            # O método pop() remove e retorna o último item da lista
            item = self.itens.pop()
            print(f'Item {item} desempilhado. Pilha: {self.itens}')
            return item

    def topo(self):
        # Retorna o item do topo da pilha sem removê-lo
        if self.is_vazia():
            print("A pilha está vazia. Não há topo.")
            return None
        return self.itens[-1]  # O topo está no último índice da lista

    def tamanho(self):
        # Retorna o número de itens na pilha
        return len(self.itens)

    def imprimir_pilha(self):
        # Imprime os elementos da pilha
        if self.is_vazia():
            print("A pilha está vazia.")
        else:
            print(f'Pilha: {self.itens}')

# Exemplo de uso da pilha
pilha = Pilha()

# Empilhar alguns itens
pilha.empilhar(10)   # Empilha 10
pilha.empilhar(20)   # Empilha 20
pilha.empilhar(30)   # Empilha 30

# Ver o topo da pilha
print(f'Topo da pilha: {pilha.topo()}')

# Desempilhar um item
pilha.desempilhar()   # Remove o item no topo

# Imprimir o estado atual da pilha
pilha.imprimir_pilha()

# Verificar o tamanho da pilha
print(f'Tamanho da pilha: {pilha.tamanho()}')

# Desempilhar todos os itens
pilha.desempilhar()   # Remove 20
pilha.desempilhar()   # Remove 10
pilha.desempilhar()   # Tenta remover da pilha vazia

# Imprimir o estado da pilha novamente
pilha.imprimir_pilha()
