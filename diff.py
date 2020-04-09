"""Nested Functions, Funções dentro de funções"""

from difflib import ndiff
from typing import List, NoReturn

def file_diff(file_1: str, file_2: str) -> NoReturn:

    def read_file(file: str) -> List:
        """
        Abre o arquivo e faz a leitura das linhas, retirando as virgulas
        """
        return [e.replace(',', '')
                for e in open(file).readlines()]

    content1 = read_file(file_1)
    content2 = read_file(file_2)
    print(''.join(ndiff(content1, content2)))


if __name__ == '__main__':
    file_diff('text1.txt', 'text2.txt')