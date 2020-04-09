class Ponto(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"Ponto({self.x +1}, {self.y +1})"      # retorna a string "Ponto(2, 3)"
                                                       # que pode ser usado como comando pelo eval


if __name__ == '__main__':
    p1 = Ponto(1, 2)
    p2 = eval(repr(p1))   # repr(p1) - devolve uma string, eval tenta executar essa string como um comando
                          # eval executa -> Ponto(2, 3) e o resultado de p2 se torna (2, 3) pois x=2 e y=3
    print(p1)
    print(p2)        # print chama __str__ que simplesmente retorna (x, y)
    print(p1.__dict__)

x = 2
print(eval("x+3"))  # eval tenta executar uma string como um comando python válido