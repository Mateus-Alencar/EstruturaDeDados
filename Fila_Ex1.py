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

fila = []
inserir(fila, 10)
inserir(fila, 20)
inserir(fila, 30)

mostrarConteudo(fila)
print(verificarItem(fila, 20))
print(totalElementos(fila))

