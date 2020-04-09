from typing import Callable, Any
from itertools import takewhile

soma2 = lambda x: x + 2

def reaplica(func: Callable, val: Any) -> Any:
    """Função que reaplica a função ao resultado da chamada."""
    return func(
        func(val)
    )


def seleciona(op: str) -> Callable:
    """Seleciona uma função, usando seu nome."""
    ops = {
        'sum': lambda x, y: x + y,
        'mul': lambda x, y: x * y
    }
    return ops[op]


words = ['water', 'afraid', 'show', 'music']

def takeWhile_condition(func, values):
    for val in values:
        if func(val):
            yield val
        else:
            break


if __name__ == '__main__':
    print(reaplica(soma2, 0))
    print(seleciona('mul')(1, 2))
    print(sorted(words))

    print(list(takewhile(lambda x: x < 10, [3, 4, 6, 10])))

    print(list(takeWhile_condition(lambda x: x < 10, [1, 3, 4, 5, 10])))
