""" iter(object, sentinel)
    object: whose iterator has to be created(sets, tuples, list)
    sentinel: optional, represent the end of a sequence"""

vowels = ['a', 'e', 'i', 'o', 'u']
vowels_iter = iter(vowels)

print(next(vowels_iter),
      next(vowels_iter),
      next(vowels_iter),
      next(vowels_iter),
      next(vowels_iter))


class PrintNumber:
    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        try:
            if self.num >= self.max:
                raise StopIteration
            self.num += 1
            return self.num
        except:
            return 'Não há mais valores para iterar'


print_num = PrintNumber(3)
print_num_iter = iter(print_num)
print(next(print_num_iter),
      next(print_num_iter),
      next(print_num_iter))
print(next(print_num_iter))


