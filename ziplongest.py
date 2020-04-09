from itertools import zip_longest

abc = ['a', 'b', 'c', 'd', 'e']
xyz = ['x', 'y', 'z', 'w', 'r']
num = ['1', '2', '3', '4', '5']

combine = (''.join(a + b + c for a, b, c in zip_longest(abc, xyz, num, fillvalue='')))

print(combine)
