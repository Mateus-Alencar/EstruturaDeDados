# Big O

Big O descreve como o tempo ou o uso de memória de um algoritmo cresce conforme o tamanho da entrada aumenta

A Notação Big O é uma forma de medir a eficiência de um algoritmo, indicando:
- Quanto tempo ele leve para executar;
- Ou quanto espaço (memória) ele consome;

Exemplo: 
```python
for i in range(n):
    print(i)
```
Se `n` = 10 -> 10 execuções.
Se `n` = 1000 -> 1000 execuções.

## O(log n) — Logarítmica
A cada passo, o problema é dividido. (Bsuca binária)

## O(n) — Linear
É aquele algoritmo cujo tempo de execução cresce proporcionalmente ao tamanho da entrada.
```python
for item in vetor:
    print(item)
```

## O(n²) — Quadrática
É um algoritmo que executa um número de operações proporcional ao quadrado do tamanho da entrada, **geralmente por causa de laços aninhados**.
```python
for i in range(n):
    for j in range(n):
        print(i, j)
```

## O(2ⁿ) — Exponencial
Explosão de possibilidades (recursão sem controle).
**Problema do caixeiro viajante** - O desafio é descobrir qual ordem gera o menor custo total.
Exemplo:
- 5 cidades → 24 caminhos
- 10 cidades → 362.880
- 15 cidades → ~87 bilhões