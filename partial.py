from functools import partial

def soma(x, y):
    return x + y


nova_soma = partial(soma, 0)  # Atribuindo um valor padrão para x
print(nova_soma(5))

nova_soma2 = partial(soma, y=3)  # Atribuindo um valor padrão para y.
print(nova_soma2(5))
print(nova_soma2(5, y=10))


print('\nSistema de Compras com partial')


def compra(total, **kwargs):
    desconto = kwargs.get('desconto')
    taxa = kwargs.get('taxa')
    if desconto:
        total -= total * (desconto / 100)

    if taxa:
        total += total * (taxa / 100)

    return total


total_compra = compra(121)
print(total_compra)

total_compra = compra(121, taxa=5)
print(total_compra)

total_compra = compra(100, taxa=10, desconto=10)
print(total_compra)


def partial1(compra, total, taxa, desconto):
    def compra_nova(total=total, taxa=taxa, desconto=desconto):
        return compra(total, taxa=taxa, desconto=desconto)
    return compra_nova


compra_nova = partial1(compra, 550, 0, 0)

print('\nCompras Novas')
print(compra_nova(1000, desconto=20, taxa=20))
print(compra_nova(1000, desconto=20))
print(compra_nova(1000, taxa=20))
print(compra_nova(1000))
print(compra_nova())