soma = lambda a, b: a + b
print(soma(1, 2))

num = 10
calc = lambda a: num + a
num = 20
calc2 = lambda a: num + a

print(calc(10))
print(calc2(10))

print("\nSHADOW VARIABLES")

num = 10
calc3 = lambda a, num=num: num + a
num = 20
calc4 = lambda a, num=num: num + a
print(calc3(10))
print(calc4(10))
