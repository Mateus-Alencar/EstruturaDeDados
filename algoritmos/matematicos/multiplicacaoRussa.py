# Multiplicação Russa utilizando uma função recursiva.
def multiplicacaoRussa(n,x):
    if n==0:
        return 0
    if n%2!=0:
        return x + multiplicacaoRussa(n//2, x*2)
    else:
        return multiplicacaoRussa(n//2, x*2)
        
def multiplicacaoRussa2(a,b):
    resultado =0
    while a > 0:
        if a % 2 != 0:
            resultado += b
        a //= 2
        b *= 2
    return resultado

print(multiplicacaoRussa(13,18))
print(multiplicacaoRussa2(13, 18))
