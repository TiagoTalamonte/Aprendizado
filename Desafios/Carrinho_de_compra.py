# Dicionário de produtos
produtos = {
    1: ("Açúcar", 7.50),
    2: ("Sal", 8.50),
    3: ("Coca Cola", 12.00),
    4: ("Coca Cola Zero", 12.00),
    5: ("Barra de Cereal", 6.50),
    6: ("Suco de Laranja", 8.00),
    7: ("Chocolate", 7.50),
    8: ("Água Mineral", 4.50)
}

# Mostra os produtos disponíveis
print("Produtos disponíveis:")
for codigo, (nome, preco) in produtos.items():
    print(f"{codigo} - {nome}: R$ {preco:.2f}")

carrinho = []
total = 0.0

# Pergunta ao usuário quantos tipos de produtos deseja comprar
n = int(input("Quantos tipos de produtos deseja comprar? ").strip())

for _ in range(n):
    codigo = int(input("Digite o número do produto desejado: ").strip())
    quantidade = int(input("Digite a quantidade: ").strip())

    if codigo in produtos:
        nome, preco_unit = produtos[codigo]
        preco_total = preco_unit * quantidade
        carrinho.append((nome, preco_unit, quantidade, preco_total))
        total += preco_total
    else:
        print("Código inválido, tente novamente.")

# Exibe o carrinho formatado
print("\nItens no carrinho:")
for nome, preco_unit, quantidade, preco_total in carrinho:
    print(f"{nome:<20} {quantidade} x R$ {preco_unit:>5.2f} = R$ {preco_total:>6.2f}")

# Exibe o total da compra
print(f'\nTotal da compra: R$ {total:.2f}')
