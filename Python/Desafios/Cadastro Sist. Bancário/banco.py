def depositar(saldo, valor, extrato, /):
    """ Realizar um depósito """
    if valor <= 0:
        print("Valor de depósito inválido")
        return saldo, extrato
    
    saldo += valor
    extrato += f"Depósito: R$ {valor:.2f}\n"
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite_saques):
    """ Realizar um saque """
    if valor > saldo:
        print("Saldo insuficiente.")
    elif limite_saques <= 0:
        print("Limite de saques atingido.")
    else:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        limite_saques -= 1

    return saldo, extrato, limite_saques

def mostrar_extrato(saldo, /, *, extrato):
    """ Mostra o extrato. """
    print("\n EXTRATO")
    print(extrato if extrato else "Sem movimentações.")
    print(f"Saldo atual: R$ {float(saldo):.2f}")
    print("=" * 20)