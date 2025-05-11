
descricao='''
Desenvolver um sistema de controle de voos em um aeroporto utilizando as estruturas de dados pilha e fila. A fila será
utilizada para gerenciar as companhias aéreas na ordem do atendimento. A pilha ser utilizada para organizar os voos da
companhia.

No programa, cada companhia vai ser representada por um dicionário contendo:
“nome”: uma string com o nome da companhia
“voos”: uma pilha (lista) que vai conter os voos da companhia

Assim dentro de cada elemento da fila haverá uma pilha contendo os voos programados para a companhia, organizados
em ordem de decolagem (o próximo voo a sair fica no topo da pilha).

Cada voo também vai ser representado por um dicionário, contendo:

“código”: uma string para representar o código do voo
“destino”: uma string para representar o destino do voo
“horário”: uma string para representar o horário do voo

As seguintes funcionalidades deverão ser apresentadas no trabalho:

a. Função para incluir uma nova companhia na fila:
inserirCompanhia(fila, nomeCompanhia) – na inserção, criar o dicionário no seguinte formato: {'nome':
nomeCompanhia, 'voos': []}

b. Função para adicionar um novo voo para a companhia. O voo é adicionado no topo da pilha de voos da
companhia:
adicionarVoo(fila, nomeCompanhia, codigo, destino, horario) – na inserção criar o dicionário no seguinte
formato:
{'codigo': codigo, 'destino': destino, 'horario': horario}

c. Função para atender o último voo da pilha da primeira companhia da fila (porque é uma pilha — atendimento
LIFO: o último voo programado é o primeiro a sair):
atenderVoo(fila) - após o voo ser removido, se a pilha de voos da companhia ficar vazia, a companhia deve
ser removida da fila.

d. Função para remover a companhia da fila, independente se houver voos para a companhia:
removerCompanhia(fila,nomeCompanhia)

e. Função para cancelar um voo - encontrar e remover um voo específico da pilha da companhia, mesmo que não
esteja no topo da pilha:
cancelarVoo(fila, nomeCompanhia, codigoVoo)

f. Função para suspender um voo - encontrar um voo e colocá-lo no início da pilha de voos (como se ele fosse
adiado). Suspender não remove o voo, apenas altera sua posição na pilha.
suspenderVoo(fila, nomeCompanhia, codigoVoo)

g. Função para trocar dois voos de posição - trocar de lugar dois voos de uma mesma companhia na pilha:
trocarVoos(fila, nomeCompanhia, codigoVoo1, codigoVoo2)

h. Função para mostrar todas as companhias e seus voos:
mostrarCompanhiaVoo(fila)

i. Função para buscar todos os voos cadastrados para um determinado destino (em todas as companhias):
buscarVoosDestino(fila, destino)

j. Função para mostrar algumas estatísticas do aeroporto - quantas companhias estão na fila, quantos voos estão
cadastrados no total e qual a companhia com maior número de voos:
mostrarEstatisticas(fila)

Utilizar, obrigatoriamente, as primitivas para manipulação de pilhas e filas: push, pop, vazia, inserir, retirar, vazia_fila.
'''

# Primitivas Pilha 
def push(p, v): 
    p.append(v)

def pop(p): # Retira o último que foi inserido na Pilha
    return p.pop()

def vazia_pilha(p):
    return False if p else True
    
# Primitivas Fila 
def pushFila(f, v):
    f.append(v)  

def popFila(f): # Retira o primeiro elemento que foi colocado na Fila
    return f.pop(0) 

def vazia_fila(f):
    return False if f else True
    
filaCompanhiasVoos = [] # Fila

def adicionarCompanhia(fila, nomeCompanhia):
    dicComp = {
        "nome":  nomeCompanhia,
        "voo":[] # Pilha
    }
    pushFila(fila, dicComp)
    
def adicionarVoo(fila, nomeCompanhia, codigo, destino, horario):
    dicVoo = {
        "codigo": codigo,
        "destino": destino,
        "horario": horario
    }
    aux = []
    while not vazia_fila(fila):
        elemento = popFila(fila)
        if elemento["nome"] == nomeCompanhia:
            push(elemento["voo"], dicVoo)  
        pushFila(aux, elemento)
    while not vazia_fila(aux):
        pushFila(fila, popFila(aux))
            
def atenderVoo(fila):
    if vazia_fila(fila):
        print("Fila de companhias vazia")
        return
    companhia = popFila(fila)

    if vazia_pilha(companhia["voo"]):
        print(f"A companhia {companhia['nome']} não tem voos para atender.")
        return

    voo_atendido = pop(companhia["voo"])
    print(f"Voo atendido da companhia {companhia['nome']}: {voo_atendido}")

    if not vazia_pilha(companhia["voo"]): 
        pushFila(fila, companhia)
    else:
        print(f"A companhia {companhia['nome']} foi removida da fila (sem voos restantes).")

def removerCompanhia(fila, nomeCompanhia):
    aux = []
    while not vazia_fila(fila):
        elemento = popFila(fila)
        if elemento["nome"] != nomeCompanhia:
            pushFila(aux, elemento)
        else:
            print(f"Companhia {elemento['nome']} retirada da lista!")
    while not vazia_fila(aux):
        elemento =  popFila(aux)
        pushFila(fila, elemento)
        
def cancelarVoo(fila, nomeCompanhia, codigoVoo):
    aux = []
    while not vazia_fila(fila):
        companhia = popFila(fila)
        if companhia["nome"] == nomeCompanhia:
            pilha_temporaria = []
            while not vazia_pilha(companhia["voo"]):
                voo = pop(companhia["voo"])
                if voo["codigo"] != codigoVoo:
                    push(pilha_temporaria, voo)
            while not vazia_pilha(pilha_temporaria):
                push(companhia["voo"], pop(pilha_temporaria))
        pushFila(aux, companhia)
    while not vazia_fila(aux):
        pushFila(fila, popFila(aux))

def suspenderVoo(fila, nomeCompanhia, codigoVoo):
    pass

def trocarVoos(fila, nomeCompanhia, codigoVoo1, codigoVoo2):
    pass

def mostrarCompanhiaVoo(fila):
    aux = []
    while not vazia_fila(fila):
        companhia = popFila(fila)
        pushFila(aux, companhia)

        print("-=-=-=-=-=-=-=-=")
        print("Companhia:", companhia["nome"])
        print("Voos programados:")
        print("-=-=-=-=-=-=-=-=")

        auxPilha = []
        while not vazia_pilha(companhia["voo"]):
            voo = pop(companhia["voo"])
            print(f"  Código : {voo['codigo']}")
            print(f"  Horário: {voo['horario']}")
            print(f"  Destino: {voo['destino']}")
            print("  -------------------")
            push(auxPilha, voo)

        while not vazia_pilha(auxPilha):
            push(companhia["voo"], pop(auxPilha))

    while not vazia_fila(aux):
        pushFila(fila, popFila(aux))


def buscarVoosDestino(fila, destino):
    filaAux = []
    while not vazia_fila(fila):
        companhia = popFila(fila)
        pushFila(filaAux, companhia)
        pilha_voo = companhia["voo"]
        aux_pilha_voo = []
        while not vazia_pilha(pilha_voo):
            voo = pop(pilha_voo)
            if voo["destino"] == destino:
                print(f"Companhia: {companhia['nome']} | Código: {voo['codigo']} | Horário: {voo['horario']}")
            push(aux_pilha_voo, voo)
        while not vazia_pilha(aux_pilha_voo):
            push(pilha_voo, pop(aux_pilha_voo))

    while not vazia_fila(filaAux):
        pushFila(fila, popFila(filaAux))

            


def mostrarEstatisticas(fila):
    pass


adicionarCompanhia(filaCompanhiasVoos, "123Milhas")
adicionarCompanhia(filaCompanhiasVoos, "GOL")
adicionarCompanhia(filaCompanhiasVoos, "AZUL")

adicionarVoo(filaCompanhiasVoos, "123Milhas", 1203, "Brasilia", "12:40")
adicionarVoo(filaCompanhiasVoos, "123Milhas", 7863, "São Paulo", "12:40")
adicionarVoo(filaCompanhiasVoos, "GOL", 1246, "Restinga", "12:40")
adicionarVoo(filaCompanhiasVoos, "AZUL", 3527, "Bielorussia", "12:40")
adicionarVoo(filaCompanhiasVoos, "GOL", 8656, "Ceara", "12:40")
adicionarVoo(filaCompanhiasVoos, "GOL", 7545, "Piaui", "12:40")
adicionarVoo(filaCompanhiasVoos, "GOL", 3885, "Aparecida do Norte", "12:40")
adicionarVoo(filaCompanhiasVoos, "GOL", 5435, "Sul", "12:40")
adicionarVoo(filaCompanhiasVoos, "123Milhas", 9765, "São Paulo", "12:40")
adicionarVoo(filaCompanhiasVoos, "AZUL", 9637, "Piaui", "12:40")

#removerCompanhia(filaCompanhiasVoos, "AZUL")

mostrarCompanhiaVoo(filaCompanhiasVoos)

#cancelarVoo(filaCompanhiasVoos, "GOL", 344365353)
print("*************************************************************")

buscarVoosDestino(filaCompanhiasVoos, "São Paulo")

    

    
