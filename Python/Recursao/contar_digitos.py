def contar_digitos(n):
    # Garante que o número é positivo
    n = abs(n)

    # Caso base: se o número for menor que 10, ele tem apenas 1 dígito
    if n < 10:
        return 1
    else:
        # Remove o último dígito e soma 1
        return 1 + contar_digitos(n // 10)

numero = int(input("Digite um número inteiro: "))
print(f"O número {numero} tem {contar_digitos(numero)} dígitos.")
