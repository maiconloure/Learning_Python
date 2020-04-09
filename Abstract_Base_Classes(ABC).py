import abc


# ABC é a superclasse para classes abstratas
# Uma classe abstrata nao pode ser instanciada e deve conter pelo menos um metodo abstrato


class Funcionario(abc.ABC):  # agora não é possivel instânciar a classe => Funcionario()
    def __init__(self, nome, cpf, salario):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario

    @abc.abstractmethod  ### agora get_bonificacao é obrigatorio para todas subclasse de Funcionario
    def get_bonificacao(self):
        return self._salario * 0.10


class ControleDeBonificacoes:
    def __init__(self, total=0):
        self.total = total

    def registra(self, funcionario):
        if hasattr(funcionario, 'get_bonificacao'):
            self.total += funcionario.get_bonificacao()
        else:
            print(f'instância de {funcionario.__class__.__name__} não implementa o método get_bonificação')

    @property
    def total_bonificacoes(self):
        return self.total


class Gerente(Funcionario):
    def __init__(self, nome, cpf, salario, senha, qtd_funcionarios):
        super().__init__(nome, cpf, salario)
        self._senha = senha
        self._qtd_funcionarios = qtd_funcionarios

    def get_bonificacao(self):
        return super().get_bonificacao() + 1000


if __name__ == '__main__':
    funcionario = Funcionario('Pedro', '111111111-11', 2000.0)
    print(f'bonificação funcionário: {funcionario.get_bonificacao()}')
    print(f"variaveis de funcionario: {vars(funcionario)}\n")
