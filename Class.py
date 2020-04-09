class Conta:
    def __init__(self, numero, nome, saldo=0):
        self._numero = numero
        self._nome = nome
        self._saldo = saldo

    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa

    def deposita(self, valor):
        self._saldo += valor - 0.10


class ContaCorrente(Conta):

    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 2


class ContaPoupanca(Conta):

    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 3


if __name__ == "__main__":
    c = Conta('123-4', 'joao', 1000)
    cc = ContaCorrente('123-5', 'pedro', 1000)
    cp = ContaPoupanca('123-6', 'Maria', 1000)

    c.atualiza(0.01)
    cc.atualiza(0.01)
    cp.atualiza(0.01)

    print(c._saldo, cc._saldo, cp._saldo)