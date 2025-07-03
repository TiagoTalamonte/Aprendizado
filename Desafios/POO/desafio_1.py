from abc import ABC, abstractmethod
from datetime import datetime


class Usuario:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def executar_transacao(self, conta, operacao):
        operacao.aplicar(conta)

    def vincular_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Usuario):
    def __init__(self, nome, nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.nascimento = nascimento
        self.cpf = cpf


class ContaBancaria:
    def __init__(self, numero, titular):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._titular = titular
        self._registro = Registro()

    @classmethod
    def criar(cls, titular, numero):
        return cls(numero, titular)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def titular(self):
        return self._titular

    @property
    def registro(self):
        return self._registro

    def sacar(self, valor):
        if valor <= 0:
            print("\n@@@ Valor inválido para saque. @@@")
            return False

        if valor > self.saldo:
            print("\n@@@ Saldo insuficiente. @@@")
            return False

        self._saldo -= valor
        print("\n=== Saque realizado com sucesso! ===")
        return True

    def depositar(self, valor):
        if valor <= 0:
            print("\n@@@ Valor inválido para depósito. @@@")
            return False

        self._saldo += valor
        print("\n=== Depósito realizado com sucesso! ===")
        return True


class ContaCorrente(ContaBancaria):
    def __init__(self, numero, titular, limite=500, max_saques=3):
        super().__init__(numero, titular)
        self.limite = limite
        self.max_saques = max_saques

    def sacar(self, valor):
        saques_realizados = len([
            r for r in self.registro.transacoes if r["tipo"] == Saque.__name__
        ])

        if valor > self.limite:
            print("\n@@@ Valor excede o limite de saque. @@@")
            return False

        if saques_realizados >= self.max_saques:
            print("\n@@@ Número máximo de saques atingido. @@@")
            return False

        return super().sacar(valor)

    def __str__(self):
        return f"""\
Agência:\t{self.agencia}
Conta:\t\t{self.numero}
Titular:\t{self.titular.nome}
"""


class Registro:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar(self, operacao):
        self._transacoes.append({
            "tipo": operacao.__class__.__name__,
            "valor": operacao.valor,
            "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        })


class Operacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def aplicar(self, conta):
        pass


class Saque(Operacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def aplicar(self, conta):
        if conta.sacar(self.valor):
            conta.registro.adicionar(self)


class Deposito(Operacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def aplicar(self, conta):
        if conta.depositar(self.valor):
            conta.registro.adicionar(self)
