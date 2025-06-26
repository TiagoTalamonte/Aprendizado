opcao = -1

while opcao != 0:
    opcao = int(input("[1]Sacar \n[2]Extrato \n[0]Sair \n: "))

    if opcao == 1:
        print("Aguarde, o saque está em andamento.")
    elif opcao == 2:
        print("Exibindo o extrato.")
else:
    print("Obrigado por ser nosso cliente, tenha um ótimo dia!")
