# Funções como objeto de primeira classe

func = lambda: 'resultado da função'

calc = {
    'soma': lambda x, y: x + y,
    'sub': lambda x, y: x - y,
    'mult': lambda x, y: x * y,
    'div': lambda x, y: x / y,
}


def soma(x, y):
    return x + y

def sub(x, y):
    return x - y

def mult(x, y):
    return x * y

def div(x, y):
    return x / y


calc_nomeado = {
    'soma': soma,
    'sub': sub,
    'mult': mult,
    'div': div,
}


somas = [lambda x: x + 0,
         lambda x: x + 1,
         lambda x: x + 2]


def soma1(x):
    return x + 1


if __name__ == '__main__':
    print(calc['mult'](2, 2))
    print(calc_nomeado['soma'](1, 1))
    print(somas[1](1))
    print(soma1(2))