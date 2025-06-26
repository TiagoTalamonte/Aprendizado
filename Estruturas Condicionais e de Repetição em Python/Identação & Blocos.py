# Função para sacar um valor da conta
def sacar(valor):
    saldo = 500  # Saldo inicial

    # Verifica se há saldo suficiente
    if saldo >= valor:
        print("Valor sacado!")
        print("Retire seu dinheiro na boca do caixa")
        saldo -= valor  # Atualiza o saldo (não afeta fora da função neste caso)
    else:
        print("Saldo insuficiente!")

# Solicita o valor ao usuário com tratamento básico
try:
    valor_digitado = float(input("Digite o valor que deseja sacar: "))
    sacar(valor_digitado)
except ValueError:
    print("Por favor, digite um número válido.")
