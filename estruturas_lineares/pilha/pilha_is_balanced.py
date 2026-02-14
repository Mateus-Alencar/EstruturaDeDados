#Você deve escrever uma função que verifica se uma expressão matemática está balanceada. 
#ra ser considerada balanceada, cada parêntese de abertura ( deve ter um parêntese de fechamento correspondente ).

#Sua função deve ser capaz de verificar as expressões que contêm parênteses, chaves {}, e colchetes []. 
#A função deve retornar True se a expressão for balanceada e False caso contrário.

def push(pilha, valor):
    pilha.append(valor) # Insere o elemento no final da lista
def pop(pilha):
    return pilha.pop() # Remove e retorna o último item
def is_Enpty(pilha):
    return False if pilha else True
    
def tamanho_pilha(pilha):
    aux = []
    contador = 0
    while not is_Enpty(pilha):
        contador+=1
        item = pop(pilha)
        push(aux, item)
    while not is_Enpty(aux):
        item = pop(aux)
        push(pilha,item)
    return contador
    
def is_balanceada(pilha):
    tamanhoPilha = tamanho_pilha(pilha)
    metade = tamanhoPilha / 2
    metade1_pilha = []
    metade2_pilha = []
    contador = 0
    while not is_Enpty(pilha):
        if contador < metade:
            contador+=1
            item1 = pop(pilha)
            push(metade1_pilha, item1)
        else:
            contador+=1
            item2 = pop(pilha)
            push(metade2_pilha, item2)
    print(metade1_pilha)
    print(metade2_pilha)
    aux = []
    aux2 = []
    while not is_Enpty(metade2_pilha):
        item = pop(metade2_pilha)
        push(aux, item)
    while not is_Enpty(aux):
        item = pop(aux)
        push(aux2, item)
    while not is_Enpty(aux2):
        item = pop(aux2)
        push(metade2_pilha, item)

    
    while not is_Enpty(metade2_pilha):
        item1 = pop(metade2_pilha)
        item2 = pop(metade1_pilha)
        if item1 == item2:
            continue
        else:
            return False
    return True
        
    
pilha=[1,2,3,3,2,1]
print(tamanho_pilha(pilha))
print(is_balanceada(pilha))
