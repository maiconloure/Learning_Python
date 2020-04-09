def initPessoa(inst, nome, nascimento):
    inst.nome = nome
    inst.nascimento = nascimento


def idade(inst, hoje):
    hd, hm, ha = hoje
    nd, nm, na = inst.nascimento
    x = ha - na
    return x


Pessoa = type('Pessoa', (), {'__init__': initPessoa, 'idade': idade})
print(Pessoa)

hank = Pessoa('Hank Moody', (8, 11, 1967))
print(hank)

print(hank.idade((6, 11, 2008)))
