from operator import add, mul, sub, itemgetter
from functools import reduce


print(reduce(add, [1, 2, 3, 4, 5]))
print(reduce(sub, [1, 2, 3, 4, 5]))
print(reduce(mul, [1, 2, 3, 4, 5]))

words = ['Aston', 'Python', 'Jaguar', 'Porsche', 'Audi', 'Barricade']

print(sorted(words, key=lambda string: string[-1]))
print(sorted(words,  key=itemgetter(-1)))

print('\nmap() VS reduce() VS filter()')
mapp = map(lambda x: x + x, [1, 2, 3, 4])
redd = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
filt = filter(lambda x, y: x + y, [1, 2, 3, 4, 5])

print(list(mapp))
print(filt)