def registrar_usuario(nome, idade, cidade="Desconhecida", *hobbies, ativo=True, **extras):
    print(f"👤 Nome: {nome}")
    print(f"🎂 Idade: {idade}")
    print(f"🏙️ Cidade: {cidade}")
    print(f"✅ Ativo: {ativo}")

    if hobbies:
        print("🎯 Hobbies:")
        for hobby in hobbies:
            print(f"   - {hobby}")
    
    if extras:
        print("📦 Informações adicionais:")
        for chave, valor in extras.items():
            print(f"   - {chave}: {valor}")

    print("-" * 40)

# Exemplos de uso
registrar_usuario("Ana", 30)
registrar_usuario("Lucas", 25, "São Paulo", "correr", "viajar", ativo=False)
registrar_usuario(
    "Marina", 27, "Rio de Janeiro", "pintar", "ler",
    ativo=True,
    profissao="Designer", email="marina@email.com"
)
