class Numero(object):
    def __init__(self, value):
        self.value = value

    def __call__(self):  # Age como se fosse uma função, torna o objeto "chamavel" ou "invocavel"
        return print('Função')

    def __str__(self):                  # runs with print()
            return f'{self.value}'

    def __int__(self):                  # runs with int()
            return int(self.value)

    def __float__(self):                # runs with float()
        return float(self.value)

    def __bytes__(self):               #runs with bytes() transform "int" number to byte code
        return bytes(self.value)

    def __add__(self, other):
        return self.value + other

    def __radd__(self, other):           # works similar to sum()
        if other == 0:
            return self
        else:
            return self.__add__(other)


number = Numero(3)

number()                        # por adicionar __call__ e tornalo uma funcao, se nao houver __call__ dá erro.

print(int(number))

print(float(number))

print(number.__dict__)

print(bytes(number))

print(number + 5)

number2 = Numero(4)
number3 = Numero(6)
print(sum([number, number2, number3]))  # sum(iterable, start) ->  iterable (list, tuple, dict, etc)
