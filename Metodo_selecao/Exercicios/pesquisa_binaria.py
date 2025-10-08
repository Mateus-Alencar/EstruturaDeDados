# função pesquisa_binaria pega um array ordenado e um item. Se o item
# está no array, a função retorna a sua posição. Dessa maneira, você é capaz de
# saber por qual ponto do array deve continuar

def pesquisa_binaria(lista, item):
    baixo = 0 
    alto = len(lista) - 1 
    while baixo <= alto: 
        meio = (baixo + alto) // 2 
        chute = lista[meio]
        if chute == item: 
            return meio
        if chute > item: 
            alto = meio - 1
        else: 
            baixo = meio + 1
    return None

minha_lista = [1, 3, 5, 7, 9] 
print(pesquisa_binaria(minha_lista, 3)) # => 1 
print(pesquisa_binaria(minha_lista,9)) # => None 
