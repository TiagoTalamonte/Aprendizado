from banco import depositar, sacar, mostrar_extrato
from clientes import cadastrar_cliente, buscar_cliente_por_cpf
import contas

saldo = 0
extrato = ""
limite_saques = 3

menu = """
========= MENU =========
[1] Depositar
[2] Sacar
[3] Ver Extrato
[4] Cadastrar Cliente
[5] Buscar Cliente por CPF
[6] Sair
[7] Criar Nova Conta
[8] Listar Contas
========================
Escolha uma opção: """

while True:
    opcao = input(menu).lower()

    if opcao == "1":
        try:
            valor = float(input("Informe o valor do depósito: R$ "))
            saldo, extrato = depositar(saldo, valor, extrato)
        except ValueError:
            print("❌ Valor inválido.")

    elif opcao == "2":
        try:
            valor = float(input("Informe o valor do saque: R$ "))
            saldo, extrato, limite_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite_saques=limite_saques
            )
        except ValueError:
            print("❌ Valor inválido.")

    elif opcao == "3":
        mostrar_extrato(saldo, extrato=extrato)

    elif opcao == "4":
        nome = input("Nome: ")
        nascimento = input("Data de nascimento (dd/mm/aaaa): ")
        cpf = input("CPF (somente números): ")
        endereco = input("Endereço (Rua, número - Bairro - Cidade/UF): ")
        cadastrar_cliente(nome, nascimento, cpf, endereco)

    elif opcao == "5":
        cpf = input("Digite o CPF a buscar: ")
        cliente = buscar_cliente_por_cpf(cpf)
        if cliente:
            print("✅ Cliente encontrado:")
            print(cliente)
        else:
            print("❌ Cliente não encontrado.")

    elif opcao == "6":
        print("🏁 Encerrando o sistema. Até logo!")
        break

    elif opcao == "7":
        cpf = input("Informe o CPF do cliente: ")
        cliente = buscar_cliente_por_cpf(cpf)
        if cliente:
            contas.criar_conta(cpf)
        else:
            print("❌ Cliente não encontrado. Cadastre o cliente antes de criar a conta.")

    elif opcao == "8":
        contas.listar_contas()


