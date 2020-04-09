class iteravel:
    def __init__(self, sequencia):
        self.data = sequencia[::-1]

    def __next__(self):

        if not self.data:
            raise StopIteration
        return self.data.pop()

    def __iter__(self):
        return self


iterador = iteravel([1, 2, 3, 4, 5])

for num in iterador:
    print(num)

