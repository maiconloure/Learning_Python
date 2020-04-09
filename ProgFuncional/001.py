# Gerar uma lista da string # Modo Imperativo

string = 'Python'
lista1 = []

for letter in string:
    lista1.append(letter)

print(lista1)  # ['P', 'y', 't', 'h', 'o', 'n']


# Gerar um lista da string # Modo Funcional

string = lambda x: x

lista = list(map(str, string('Python')))

print(lista)  # ['P', 'y', 't', 'h', 'o', 'n']