lista = [1, 2, 3, 4, 5]

print(any(lista))  # True

def any_funcionamento(iteravel):
    """Os seguintes valores são considerados falsos:
    >> None, False,
    >> Zeros: 0(int), 0.0(float), 0j(complex)
    >> Sequencias vazias: [], "", {}
    A única maneira de any retornar 'False' é se todos os elementos no iterável forem falsos.
    """
    for elemento in iteravel:
        """Os seguintes valores são considerados falsos"""
        print(elemento, bool(elemento))
    print()


any_funcionamento(lista)

# // ---------------------------------------------------------------------------------------- //

lista2 = [0, 2, 3, 4, 5]

print(all(lista))  # True
print(all(lista2))  # False

# // ---------------------------------------------------------------------------------------- //

def _len(sequencia):
    cont = 0
    for x in sequencia:
        cont += 1
    return cont

print()
print(_len([1, 2, 3, 4, 5]))  # 5

print('__len__' in dir([1, 2, 3]))
print('__len__' in dir('string'))
print('__len__' in dir(1))



