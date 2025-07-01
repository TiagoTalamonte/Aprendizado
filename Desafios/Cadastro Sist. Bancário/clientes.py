clientes = []

def cadastrar_cliente(nome, nascimento, cpf, endereco):
    """Cadastra um cliente se o CPF ainda não estiver registrado."""
    if any(c['cpf'] == cpf for c in clientes):
        print("❌ CPF já cadastrado.")
        return False
    
    cliente = {
        "nome": nome,
        "nascimento": nascimento,
        "cpf": cpf,
        "endereco": endereco
    }

    clientes.append(cliente)
    print("✅ Cliente cadastrado com sucesso!")
    return True

def buscar_cliente_por_cpf(cpf):
    """ Busca e retorna o CPF inserido """  
    for cliente in clientes:
        if cliente["cpf"] == cpf:
            return cliente
        return None

