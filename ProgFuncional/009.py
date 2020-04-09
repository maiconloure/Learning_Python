def map_clone(function, sequence):
    """
    Função geradora, clone do map
    """
    for elem in sequence:
        yield function(elem)


func1 = list(map_clone(lambda x: x ** 2, [1, 2, 3]))


def f_geradora():
    yield 1
    yield 2
    yield 3
    yield 4


gen = f_geradora()
print(list(gen))  # [1, 2, 3, 4]


def gen():
    for elem in [[1, 2, 3], [4, 5, 6], [7, 8, 9]]:
        yield elem


def gen_flat():
    for elem in [[1, 2, 3], [4, 5, 6], [7, 8, 9]]:
        yield from elem


print(list(gen()))
print(list(gen_flat()))


# Hora, Minuto, Segundos
tempo = [(13, 17, 50),
         (17, 28, 51),
         (2, 28, 51),
         (23, 27, 26)]

hora = lambda x: (x[0] % 12, 'pm') if x[0] > 12 else (x[0] % 12, 'am')
formato = lambda x, y: (y[0], x[1], x[2], y[1])


def func_map(seq, *funcs):
    for elem in seq:
        yield funcs[1](elem, funcs[0](elem))  # formato((13,17,50), hora((13,17,50) -> formato((13,17,50), (1, 'pm')
                                              # (1, 17, 50, 'pm')


print(list(func_map(tempo, hora, formato)))


def map_reduce(map_func, reduce_func, sequence):
    return reduce_func(map_func(sequence))

map_func = lambda x: ((elem, 1) for elem in x)

def reduce_func(sequence):
    dicio = {}
    for key, val, in sequence:
        if key not in dicio:
            dicio[key] = val
        else:
            dicio[key] += val

    return dicio

print(map_reduce(map_func, reduce_func, 'abacaxi'))
print(map_reduce(map_func, reduce_func, 'abacaxi verde limão verde como coco verde'.split()))


from collections import Counter

print(Counter('abacaxi'))
print(Counter('abacaxi verde limão verde como coco verde'.split()))


testando = map_reduce(map_func, reduce_func, 'marmelada')
print(testando)
ordenando = {key: value for key, value in sorted(testando.items(), key=lambda item: item[1], reverse=True)}
print(ordenando)

for key, value in (testando.items()):
    print(key, value)











