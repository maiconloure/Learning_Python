from operator import itemgetter
from itertools import filterfalse

print('SORT e SORTED')  # //---------------------------------------------------------//
lista1 = [1, 2, 3, 3, 2, 1]
lista1.sort()
print(lista1)
autores = (('Fernando', 17, 'Portugal'),
           ('Drummond', 14, 'Brazil'),
           ('Altro', 4, 'Brazil'))

print(sorted(autores))
print(sorted(autores, key=lambda x: x[0][-1]))
print(sorted(autores, key=lambda x: x[0][-1], reverse=True))

print(sorted(autores, key=itemgetter(1)))

print('\nFILTER')  # //---------------------------------------------------------//
lista2 = [1, 2, 3, 4, 5]
impares = lambda x: x % 2   # retorna 0 se for par, e 0 é False,
                            # False não é retornado por filter()

print(list(filter(impares, lista2)))  # [1, 3, 5]

print(list(filterfalse(impares, lista2)))  # Agora apenas False é retornado







