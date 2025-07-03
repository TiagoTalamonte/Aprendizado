# Classe Conta representa uma conta bancária simples.
# - Possui atributos: nro_agencia (público) e _saldo (privado).
# - Métodos:
#   - depositar(valor): adiciona valor ao saldo.
#   - sacar(valor): subtrai valor do saldo.
#   - mostrar_saldo(): retorna o saldo atual.
# Exemplo de uso:
#   conta = Conta("0001", 100)
#   conta.depositar(100)
#   print(conta.nro_agencia)        # imprime "0001"
#   print(conta.mostrar_saldo())    # imprime 200

# Define a classe Conta, que representa uma conta bancária simples
class Conta:
    # Método construtor, chamado ao criar uma nova instância da classe
    def __init__(self, nro_agencia, saldo=0):
        self._saldo = saldo           # Atributo privado que armazena o saldo da conta
        self.nro_agencia = nro_agencia  # Atributo público com o número da agência

    # Método para depositar um valor na conta
    def depositar(self, valor):
        # Adiciona o valor ao saldo
        self._saldo += valor

    # Método para sacar um valor da conta
    def sacar(self, valor):
        # Subtrai o valor do saldo
        self._saldo -= valor

    # Método para retornar o saldo atual da conta
    def mostrar_saldo(self):
        return self._saldo


# Cria uma nova conta da agência "0001" com saldo inicial de 100
conta = Conta("0001", 100)

# Realiza um depósito de 100 na conta
conta.depositar(100)

# Exibe o número da agência
print(conta.nro_agencia)

#
