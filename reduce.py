from functools import reduce
list_numbers = [1, 3, 4, 5, 6, 7, 8, 9]

def soma(x, y):
    return x + y


soma = reduce(soma, list_numbers)
print(soma)

zero = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
print(zero)  