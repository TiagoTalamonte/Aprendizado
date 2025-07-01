# *args: recebe uma lista de nomes dos usuários.
# **kwargs: recebe os dados adicionais para cada usuário. Cada chave do kwargs é o nome de um usuário, e o valor é um dicionário com os dados.
def cadastrar_usuarios(*args, **kwargs):
    print("📋 Iniciando cadastro de usuários...")
    
    if not args:
        print("⚠️ Nenhum nome de usuário foi informado.")
        return

    for i, nome in enumerate(args, 1):
        print(f"\n👤 Usuário {i}: {nome}")
        # Verifica se existem parâmetros específicos para esse usuário
        if nome in kwargs:
            dados = kwargs[nome]
            for chave, valor in dados.items():
                print(f"   - {chave}: {valor}")
        else:
            print("   - Nenhum dado extra fornecido.")

# Exemplo de uso:
cadastrar_usuarios(
    "Alice", "Bob", "Carlos",
    Alice={"idade": 28, "email": "alice@example.com"},
    Bob={"idade": 34, "telefone": "99999-9999"},
    Carlos={"email": "carlos@example.com"}
)
