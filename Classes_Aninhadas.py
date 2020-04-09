# Inner or Nested Classes

class Ponto(object):
    def __init__(self):
        self.ponto = '.'

    def __str__(self):
        return self.ponto

    class PontoVirgula(object):
        def __init__(self):
            self.pontovirgula = ';'

        def f(self):
            return self.pontovirgula


obj = Ponto.PontoVirgula()
print(obj.f())
obj = Ponto()
print(obj)