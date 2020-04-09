class Funcionario(object):
    def __init__(self, nome, cpf, salario):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario

    def get_bonificacao(self):
        return self._salario * 0.10


class Gerente(Funcionario):
    def __init__(self, nome, cpf, salario, senha, qtd_funcionarios):
        super().__init__(nome, cpf, salario)
        self._senha = senha
        self._qtd_funcionarios = qtd_funcionarios

    def get_bonificacao(self):
        return super().get_bonificacao() + 1000


class ControleDeBonificacoes:
    def __init__(self, total=0):
        self.total = total

    def registra(self, funcionario):          ### hasattr(objeto, atributo) verifica se o objeto possui aquele atributo
        if hasattr(funcionario, 'get_bonificacao'):         ### se o attr está em __dict__ do objeto
            self.total += funcionario.get_bonificacao()
        else:
            print(f'instância de {funcionario.__class__.__name__} não implementa o método get_bonificação')

    @property
    def total_bonificacoes(self):
        return self.total


funcionario = Funcionario('Pedro', '111111111-11', 2000.0)
print(f'bonificação funcionário: {funcionario.get_bonificacao()}')
print(f"variaveis de funcionario: {vars(funcionario)}\n")
                                                                ### vars() retorna __dict__ do objeto especificado
gerente = Gerente('Jose', '222222222-22', 5000.0, '1234', 0)
print(f'bonificação gerente: {gerente.get_bonificacao()}')
print(f"variaveis de gerente: {vars(gerente)}")

controle = ControleDeBonificacoes()
controle.registra(funcionario)
controle.registra(gerente)

print(f'Total: {controle.total_bonificacoes}')


class Cliente(object):
    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade


print()
cliente = Cliente('Maria', '33333333-33', '1234')
controle.registra(cliente)

var = [x for x in dir(funcionario)]    ### dir() tenta retornar uma lista de atributos válidos do objeto

print(f"\nlista de atributos de Funcionario(superclasse): \n{str(var[0:9])[1:-1]}"
                                                        f"\n{str(var[9:19])[1:-1]}"
                                                        f"\n{str(var[19:])[1:-1]}")