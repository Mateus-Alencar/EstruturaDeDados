def mostrar_binario(n):
    # Caso base: quando o número é 0 ou 1
    if n < 2:
        print(n, end='')
    else:
        mostrar_binario(n // 2)  # Chamada recursiva dividindo o número por 2
        print(n % 2, end='')     # Mostra o resto (0 ou 1)


numero = int(input("Digite um número inteiro: "))
print(f"Representação binária de {numero}: ", end='')
mostrar_binario(numero)
print()  
