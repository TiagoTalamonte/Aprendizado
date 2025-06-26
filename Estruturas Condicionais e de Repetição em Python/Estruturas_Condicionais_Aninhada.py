tipo = input("Digite o tipo de conta (universitaria ou normal): ").lower()

conta_normal = tipo == "normal"
conta_universitaria = tipo == "universitaria"

if not (conta_normal or conta_universitaria):
    print("Erro: tipo de conta inválido. Digite 'normal'ou 'universitaria'.")
else:
    saque = int(input("Informe a quantia do seu saque: "))
    saldo = 2000
    cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com o Cheque especial!")
    else:
        print("Saldo insuficiente!")

elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente!")
        
