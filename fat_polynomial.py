from sympy.abc import x
from sympy import factor

result = factor(x**2 + 3*x)
print(result)

result1 = factor(x**2 - 9)
print(result1)

result2 = factor(x**2 - 4 * x + 4)
print(result2)

