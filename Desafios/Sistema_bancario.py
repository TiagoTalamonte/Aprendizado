saldo = 0.0
extrato = []
limite_saque = 3
saques_realizados = 0
LIMITE_POR_SAQUE = 500.00

def menu():
    print("\n=== SISTEMA BANCÁRIO ===")
    print("[1] Depositar")
    print("[2] Sacar")
    print("[3] Ver Extrato")
    print("[0] Sair")

while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        valor = float(input("Digite o valor para depósito: R$ "))
        if valor > 0:
            saldo += valor
            extrato.append(f"Depósito: +R$ {valor:.2f}")
            print("Depósito realizado com sucesso!")
        else:
            print("Valor inválido!")

    elif opcao == "2":
        if saques_realizados >= limite_saque:
            print("❌ Limite diário de saques atingido.")
            continue

        valor = float(input("Digite o valor para saque: R$ "))
        if valor <= 0:
            print("Valor inválido!")
        elif valor > saldo:
            print("❌ Saldo insuficiente.")
        elif valor > LIMITE_POR_SAQUE:
            print(f"❌ Limite por saque é R$ {LIMITE_POR_SAQUE:.2f}.")
        else:
            saldo -= valor
            extrato.append(f"Saque: -R$ {valor:.2f}")
            saques_realizados += 1
            print("Saque realizado com sucesso!")

    elif opcao == "3":
        print("\n=== EXTRATO ===")
        if not extrato:
            print("Nenhuma movimentação.")
        else:
            for item in extrato:
                print(item)
        print(f"Saldo atual: R$ {saldo:.2f}")

    elif opcao == "0":
        print("Obrigado por usar o sistema bancário. Até logo!")
        break

    else:
        print("Opção inválida. Tente novamente.")
