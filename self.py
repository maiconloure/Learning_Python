# O porquê do self explícito em Python

from functools import partial

def newClass(nome, atributos):
    cls = {}
    for k, v in atributos.items():
        cls[k] = v
    return cls


def newPessoa(nome, nascimento):
    inst = {}
    inst['classe'] = Pessoa

    for k, v in Pessoa.items():
        if callable(v):
            metodo = partial(v, inst)
            inst[k] = metodo

    inst['nome'] = nome
    inst['nascimento'] = nascimento
    return inst


def idade(inst, hoje):
    hd, hm, ha = hoje
    nd, nm, na = inst['nascimento']
    x = ha - na
    return x


Pessoa = newClass('Pessoa', {'newPessoa': newPessoa, 'idade': idade})
# cls{'newPessoa': newPessoa(nome, nascimento), 'idade': idade(inst, hoje)} # FIM DA DEFINICAO DE CLASSE

hank = Pessoa['newPessoa']('Hank Moody', (8, 11, 1967))
# hank{'classe': Pessoa{'newPessoa: newPessoa(inst), 'idade': idade()}, 'nome':


idade(hank, (6, 11, 2008))
Pessoa['idade'](hank, (6, 11, 2008))
hank['classe']['idade'](hank, (6, 11, 2008)) #TODOS OS 3 imprimem a idade == 41


print(hank['nome'])
print(hank['nascimento'])
print(Pessoa)
print(hank)

###################################################################### TUDO ISSO EQUIVALE
###################################################################### A ISSO

class Pessoa(object):
    def __init__(self, nome, nascimento):
        self.nome = nome
        self.nascimento = nascimento

    def idade(self, hoje):
        hd, hm, ha = hoje
        nd, nm, na = self.nascimento
        x = ha - na
        return x


hank2 = Pessoa('Hank Moody', (8, 11, 1967))
print(hank2.idade((6, 11, 2008)))