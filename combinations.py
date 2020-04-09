from itertools import product

caracteres = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
combinations = list(product(caracteres, repeat=4))

print(combinations)
print(len(combinations))

combination2 = [''.join(str(i) for i in x) for x in product(caracteres, repeat=4)]
print(combination2)
print(len(combination2))
