
# 📘 Funções Recursivas

## 🔹 O que é Recursão?
Recursão é uma técnica de programação onde uma função **chama a si mesma** para resolver um problema.  
Ela é especialmente útil quando o problema pode ser dividido em **subproblemas menores e semelhantes**.

---

## 🔹 Estrutura de uma Função Recursiva
Uma função recursiva deve ter **duas partes principais**:

1. **Caso base (condição de parada):**  
   - Impede chamadas infinitas da função.  
   - Define quando a recursão deve parar.

2. **Chamada recursiva:**  
   - A função chama a si mesma com um **problema menor**, aproximando-se do caso base.

📌 Exemplo em Python:

```python
def fatorial(n):
    if n == 0 or n == 1:  # Caso base
        return 1
    else:
        return n * fatorial(n - 1)  # Chamada recursiva

print(fatorial(5))  # Saída: 120
```

---

## 🔹 Exemplos Clássicos de Recursão

### 1. Fatorial
```python
def fatorial(n):
    if n == 0:
        return 1
    return n * fatorial(n - 1)
```

### 2. Sequência de Fibonacci
```python
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
```

### 3. Contagem Regressiva
```python
def contagem(n):
    if n == 0:
        print("🚀 Fogo!")
    else:
        print(n)
        contagem(n - 1)
```

---

## 🔹 Vantagens
✅ Código mais **curto** e **expressivo**.  
✅ Facilita a resolução de problemas que têm natureza **divisível em subproblemas** (ex: árvores, grafos).  

---

## 🔹 Desvantagens
- Pode causar **estouro de pilha** se não houver caso base.  
- Pode ser **menos eficiente** que uma solução iterativa (devido ao custo de chamadas de função).  

---

## 🔹 Recursão vs Iteração
- **Recursão:** divide o problema em partes menores e chama a si mesma.  
- **Iteração:** utiliza estruturas como `for` ou `while`.  

📌 Exemplo: cálculo de fatorial

**Iterativo:**
```python
def fatorial_iterativo(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado
```

**Recursivo:** (já visto acima)

---

## 🔹 Quando Usar Recursão?
- Quando o problema tem **natureza recursiva** (árvores, grafos, algoritmos de busca).  
- Quando a **clareza do código** é mais importante que a performance.  
- Quando a **solução iterativa é muito complexa**.  

---

## 📌 Conclusão
Funções recursivas são uma poderosa ferramenta para resolver problemas que podem ser quebrados em partes menores.  
Porém, devem ser usadas com cuidado para evitar **ineficiências** e **estouro de pilha**.
