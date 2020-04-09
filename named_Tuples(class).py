from collections import namedtuple

Car = namedtuple('Car', 'color year')

jaguar = Car('Black', '2020')
print(jaguar.color)
print(jaguar.year)