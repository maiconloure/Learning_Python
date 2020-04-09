"""Transformando um string de numeros, em uma lista
com conjunto de numeros separads por \n"""

matrix = "1 2 3 4\n4 5 6 5\n7 8 9 6\n8 7 6 7"
print(matrix)
matrix = matrix.split("\n")
print(matrix)
matrix2 = []
for n in range(len(matrix)):
    matrix[n] = matrix[n].split()
    matrix[n] = list(map(int, matrix[n]))  # EX: Tranforma a string '1' em um inteiro
    matrix2.append(matrix[n][0])  # Pegar o primeiro elemento/numero de cada indice

for index in range(4):
    print(matrix[index])

print()
print(matrix2)