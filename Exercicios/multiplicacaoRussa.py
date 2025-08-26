# Multiplicação Russa utilizando uma função recursiva.
def multiplicacaoRussa(n,x):
    if n==0:
        return 0
    if n%2!=0:
        return x + multiplicacaoRussa(n//2, x*2)
    else:
        return multiplicacaoRussa(n//2, x*2)
        
print(multiplicacaoRussa(42,35))
