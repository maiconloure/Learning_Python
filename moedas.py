import locale


def converte_real_para_euro(valor):
    return valor / 5.26


def converte_real_para_dolar(valor):
    return valor / 4.64


valor_inicial = 50.0
print(valor_inicial)
valor_em_euro = converte_real_para_euro(valor_inicial)
print(valor_em_euro)

# Metodo manual /----------------------------------/
arredonda = round(valor_em_euro, 2)
virgula = str(arredonda).replace('.', ',')
formatado = f'{virgula} €'
print(formatado)

# Módulo Locale /----------------------------------/

locale.setlocale(locale.LC_MONETARY, 'en_US.UTF-8')
valor_em_dolar = converte_real_para_dolar(valor_inicial)
dolar = locale.currency(valor_em_dolar)
print(dolar)
dolar = locale.currency(15000.0, grouping=True)  # international=True para mostrar USD
print(dolar)


