# Primitivas Pilha 
def push(p, v): 
    p.append(v)

def pop(p): # Retira o último que foi inserido na Pilha
    return p.pop()

def vazia(p):
    return False if p else True
    
# Primitivas Fila 
def pushFila(f, v):
    f.append(v)  

def popFila(f): # Retira o primeiro elemento que foi colocado na Fila
    return f.pop(0) 

def vazia_fila(f):
    return False if f else True
    
filaVoos = [] # Fila

def adicionarCompanhia(fila, nomeCompanhia):
    dicComp = {
        "nome":  nomeCompanhia,
        "voo":[]
    } # Pilha
    pushFila(filaVoos, dicComp)
    
def adicionarVoo(fila, nomeCompanhia, codigo, destino, horario):
    pass

adicionarCompanhia(filaVoos, "123Milhas")
adicionarCompanhia(filaVoos, "GOL")
adicionarCompanhia(filaVoos, "AZUL")

for x in filaVoos:
    print(x)

    
