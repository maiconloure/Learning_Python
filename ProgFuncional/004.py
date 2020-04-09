list_comp = [elem + 2 for elem in [1, 2, 3, 4, 5]]  # [3, 4, 5, 6, 7]

lista = [1, 2, 3, 4, 5]
list_for = []  # [3, 4, 5, 6, 7]

for elem in lista:
    list_for.append(elem + 2)

# /-----------------------------------/

def soma2(num):
    return num + 2


gen_def = map(soma2, [1, 2, 3, 4, 5])  # <map object at 0x010DB1D8>

gen_lambda = map(lambda x: x+2, [1, 2, 3, 4, 5])  # <map object at 0x010DB268>

generator_exp = (x + 2 for x in [1, 2, 3, 4, 5])  # <generator object <genexpr> at 0x010EB878>

if __name__ == '__main__':
    print(list_comp)
    print(list_for)
    print(gen_def)
    print(gen_lambda)
    print(generator_exp)
