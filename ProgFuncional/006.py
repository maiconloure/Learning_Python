lista = [1, 2, 3, 4, 5]
lista_inversa = reversed(lista)  # <list_reverseiterator object at 0x0362B160>

nova_lista = list(zip(lista, lista_inversa))  # [(1, 5), (2, 4), (3, 3), (4, 2), (5, 1)]

# // ---------------------------------------------------------------------------------------- //

enumera = list(enumerate([1, 2, 3, 4, 5]))  # [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]

# // ---------------------------------------------------------------------------------------- //

def func(num):
    return num + 2


mapeando = list(map(func, [0, 1, 2, 3, 4]))
mapbool = list(map(bool, [0, 1, 2, 3, 4]))

if __name__ == '__main__':
    print(list(reversed(lista)))
    print(lista_inversa)
    print(nova_lista)
    print()
    print(enumera)
    print()
    print(mapeando)
    print(mapbool)
