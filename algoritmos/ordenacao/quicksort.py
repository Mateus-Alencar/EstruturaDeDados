def quick_sort(lista):
  if len(lista) < 2:
    return lista
  pivo = lista[len(lista) // 2]
  menores = []
  maiores = []
  iguais = []
  for x in lista:
    if x > pivo:
      maiores.append(x)
    elif x == pivo:
      iguais.append(x)
    else:
      menores.append(x)
  return quick_sort(menores) + iguais + quick_sort(maiores)

numeros = [10, 7, 8, 9, 1, 5]
ordenado = quick_sort(numeros)
print(ordenado)