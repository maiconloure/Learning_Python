def meu_maximo(a=0, b=0, c=0, d=0, e=0):
    return max((a, b, c, d, e))


def meu_maximo_infinito(**kwargs):
    return max(kwargs.values())


dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

print(meu_maximo(**dicionario))
print(meu_maximo_infinito(**dicionario))