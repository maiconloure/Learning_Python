# Uma lista de listas, isso em python tambêm é uma Matriz
lista1 = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]

def func(l):
    return list(reversed(l))


print(list(map(func, lista1)))  # [[2, 1], [3, 2], [4, 3], [5, 4], [6, 5]]


print('\nMAX E MIN')  # //---------------------------------------------------------//
lista2 = [[7, 2], [5, 3], [5, 4], [5, 5], [5, 6]]  # maior indice é [5,6],
                                                   # mas o maior valor está em [7,2]
print(max(lista2))  # [7, 2]

def func2(lista):
    return lista[0] + lista[1]


print(max(lista2, key=func2))  # [5, 6]
print(max(lista2, key=sum))  # [5, 6]

print(min(lista2, key=sum))  # [5, 3]

print('\nITER')  # //---------------------------------------------------------//
lista = [1, 2, 3, 4, 5]

print(list(iter(lista.pop, 3)))  # [5, 4]
# iter(...)
#     iter(iterable) -> iterator
#     iter(callable, sentinel) -> iterator
#       callable: lista.pop
#       sentinel: limite da iteração, se chegar no iteravel 3 ele para

print()
with open('mydata.txt', 'r') as fp:
    for line in iter(fp.readlines, []):
        print(line)

















