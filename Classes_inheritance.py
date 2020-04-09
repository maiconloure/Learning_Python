class Pessoa(object):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def mostrar_nome(self):
        print(self.nome)

    def mostrar_idade(self):
        print(self.idade)


class Estudante(Pessoa):
    def __init__(self, nome, idade, curso):
        Pessoa.__init__(self, nome, idade)
        self.curso = curso

    def mostrar_curso(self):
        print(self.curso)


p = Pessoa('Marcos', 30)
p.mostrar_idade()
s = Estudante('Pedro', 20, 'Programação')
s.mostrar_curso()

print()

class People(object):
    FEMALE = 0
    MALE = 1

    def __init__(self, name, genre):
        super(People, self).__init__()
        self._name = name
        self._genre = genre

    def __str__(self):
        return str(self._name)


class Father(People):
    def __init__(self, name, genre, child):
        super(Father, self).__init__(name, genre)
        self._child = child
        print(f'self._child: {self._child}')

    def getChild(self, i):
        return self._child[i]


p = People('Jack', 'MALE')
print(p)
f = Father('John', 'MALE', p)
print(f)
print(f.getChild())
