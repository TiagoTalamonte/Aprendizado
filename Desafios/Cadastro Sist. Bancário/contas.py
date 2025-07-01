# contas.py

# Lista global que armazena todas as contas criadas
contas = []
contador_contas = 1

def criar_conta(cpf):
    """Cria uma nova conta vinculada a um CPF existente."""
    global contador_contas

    conta = {
        "numero": contador_contas,
        "cpf": cpf
    }

    contas.append(conta)
    print(f"✅ Conta Nº {contador_contas} criada para CPF {cpf}")
    contador_contas += 1


def listar_contas():
    """Exibe todas as contas registradas."""
    if not contas:
        print("📭 Nenhuma conta encontrada.")
        return

    print("\n📂 CONTAS REGISTRADAS:")
    for conta in contas:
        print(f"➡️ Conta Nº: {conta['numero']} | CPF: {conta['cpf']}")
