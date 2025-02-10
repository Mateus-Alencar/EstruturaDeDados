#1. A Classe Nodo
#Essa classe define o nó de uma lista encadeada. Cada nó tem dois componentes principais:
#
#dado: O valor ou dados armazenados nesse nó.
#proximo: Um ponteiro (ou referência) para o próximo nó da lista. Inicialmente, este ponteiro é definido como None, porque ainda não há outro nó após este.

class Nodo:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None  # Ponteiro para o próximo nó

#A Classe ListaEncadeada
#Essa classe implementa a lista encadeada. Ela tem um ponteiro chamado cabeca, que aponta para o primeiro nó da lista. Quando a lista é criada, ela começa vazia, então cabeca é None.
  
class ListaEncadeada:
    def __init__(self):
        self.cabeca = None  # Inicialmente a lista está vazia

    # Inserir no início da lista
    def inserir_inicio(self, dado):
        novo_nodo = Nodo(dado)
        novo_nodo.proximo = self.cabeca
        self.cabeca = novo_nodo

    # Inserir no final da lista
    def inserir_fim(self, dado):
        novo_nodo = Nodo(dado)
        if not self.cabeca:  # Se a lista estiver vazia
            self.cabeca = novo_nodo
            return
        ultimo_nodo = self.cabeca
        while ultimo_nodo.proximo:
            ultimo_nodo = ultimo_nodo.proximo
        ultimo_nodo.proximo = novo_nodo

    # Remover o primeiro elemento da lista
    def remover_inicio(self):
        if not self.cabeca:
            print("Lista vazia!")
            return
        self.cabeca = self.cabeca.proximo

    # Imprimir todos os elementos da lista
    def imprimir_lista(self):
        nodo_atual = self.cabeca
        while nodo_atual:
            print(nodo_atual.dado, end=" -> ")
            nodo_atual = nodo_atual.proximo
        print("None")

# Exemplo de uso
lista = ListaEncadeada()
lista.inserir_inicio(10)
lista.inserir_inicio(20)
lista.inserir_fim(30)

lista.imprimir_lista()  # Output: 20 -> 10 -> 30 -> None

lista.remover_inicio()
lista.imprimir_lista()  # Output: 10 -> 30 -> None
