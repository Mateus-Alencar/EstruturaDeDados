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
    dicVoo = {
        "codigo":codigo,
        "destino":destino,
        "horario":horario
    }
    aux = []
    while not vazia_fila(fila):
        elemento = popFila(fila)
        pushFila(aux, elemento)
        if elemento["nome"] == nomeCompanhia:
            elemento["voo"] == dicVoo
    while not vazia_fila(aux):
        elemento = popFila(aux)
        pushFila(fila, elemento)
            
    

adicionarCompanhia(filaVoos, "123Milhas")
adicionarCompanhia(filaVoos, "GOL")
adicionarCompanhia(filaVoos, "AZUL")

for x in filaVoos:
    print(x)
    print(x["nome"])

    
