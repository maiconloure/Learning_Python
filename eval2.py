def calculatePerimeter(l):
    return 4*l

# Area of Square
def calculateArea(l):
    return l*l


property = input("Type a function: ")

for l in range(1, 5):
    if property == 'calculatePerimeter(l)':  #  l é o range do 'for'
        print("If length is ", l , ", Perimeter = ", eval(property))
    elif property == 'calculateArea(l)':
        print("If length is ", l , ", Area = ", eval(property)) # its the same as calculateArea(l)
    else:
        print('Wrong Function')
        break

print('\n')

from math import *

print(eval('dir()', {'sqrt': sqrt, 'pow': pow}))  # permitindo algumas funções

print(eval('dir()', {'squareRoot': sqrt, 'pow': pow}))  ## Alterando o nome da função

print(eval('squareRoot(9)', {'squareRoot': sqrt, 'pow': pow}))  # usando função renomeada

a = 5
print(eval('sqrt(a)', {'__builtins__': None}, {'a': a, 'sqrt': sqrt}))  # Passando no dicionário global e local

