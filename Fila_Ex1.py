def inserir(f, v):
    f.append(v)  # insere um valor no final da lista

def retirar(f):
    return f.pop(0)  # retira e retorna um valor do início da lista

def vazia_fila(f):
    return False if f else True
    
def totalElementos(f):
    aux = []
    contador = 0
    while not vazia_fila(f):
        item = retirar(fila)
        inserir(aux, item)
        contador += 1
    while not vazia_fila(aux):
        item = retirar(aux)
        inserir(f, item)
    return contador

def mostrarConteudo(fila):
    aux = []
    while not vazia_fila(fila):
        item = retirar(fila)
        inserir(aux, item)
        print(item)
    while not vazia_fila(aux):
        item = retirar(aux)
        inserir(fila, item)
def verificarItem(fila, item):
    aux = []
    flag = False
    while not vazia_fila(fila):
        num = retirar(fila)
        inserir(aux, num)
        if item == num:
            flag = True
    while not vazia_fila(aux):
        item = retirar(aux)
        inserir(fila, item)
        
    return flag
def intercalarFilas(fila1, fila2):
    aux1 = []
    aux2 = []
    filaIntercalada = []
    while not vazia_fila(fila1):
        num = retirar(fila1)
        inserir(filaIntercalada, num)
        inserir(aux1, num)
        while not vazia_fila(fila2):
            num2 = retirar(fila2)
            inserir(filaIntercalada, num2)
            inserir(aux2, num2)
            break
    while not vazia_fila(fila2):
            num2 = retirar(fila2)
            inserir(filaIntercalada, num2)
            inserir(aux2, num2)
    while not vazia_fila(aux1):
        item = retirar(aux1)
        inserir(fila1, item)
    while not vazia_fila(aux2):
        item = retirar(aux2)
        inserir(fila2, item)
    return filaIntercalada
        
fila = []
inserir(fila, 10)
inserir(fila, 20)
inserir(fila, 30)

mostrarConteudo(fila)
print(verificarItem(fila, 20))
print(totalElementos(fila))

fila1 = [1,2,3,11]
fila2 = [4,5,6]
print(intercalarFilas(fila1, fila2))
print(fila1)
print(fila2)

