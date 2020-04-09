from numbers import Number
from typing import Union, Any, List, Dict, Sequence, Text

Somavel = Union[Number, str, list]


def soma(x: Somavel, y: Somavel) -> Somavel:
    return x + y

def identity(val: Any) -> Any:
    return val

def my_sum(l: List[Number]) -> Number:
    return sum(l)


def user_registration(nome: str, idade: int, gostos: List[str]) -> Dict[str, Union[str, int, List[str]]]:
    return {
        'nome': nome,
        'idade': idade,
        'gostos': gostos
    }


def my_min(seq: Sequence):
    return min(seq)


def converte_bytes_para_reais(valor: Text):
    if isinstance(valor, bytes):
        print(valor.decode(), end=' = ')
    return type(valor)


if __name__ == '__main__':
    print(soma('2', '3'))
    print(identity('ABC'))
    print(my_sum([4, 2, 3, 4, 5, 6]))
    print(user_registration('eduardo', 26, ['ouvir musica', 'python']))

    print(my_min((1, 2, 3, 1, 4)))
    print(my_min([1, 2, 3, 1, 4]))
    print(my_min({1, 2, 3, 4, 1}))

    print(converte_bytes_para_reais(b'2.5'))  # o primeiro é bytes
    print(converte_bytes_para_reais('2.5'))  # o segundo apenas string
    print((b'2.4').decode())