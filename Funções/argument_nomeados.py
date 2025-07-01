# em vez de passar os valores só pela ordem, você pode passar o nome do parâmetro junto com o valor. 

def criar_pedido(*, cliente, produto, quantidade, preco_unitario, forma_pagamento="cartão"):
    total = quantidade * preco_unitario
    print(f"🧾 Pedido criado com sucesso!")
    print(f"👤 Cliente: {cliente}")
    print(f"📦 Produto: {produto}")
    print(f"🔢 Quantidade: {quantidade}")
    print(f"💰 Preço unitário: R$ {preco_unitario:.2f}")
    print(f"💳 Forma de pagamento: {forma_pagamento}")
    print(f"🧮 Total: R$ {total:.2f}")
    print("")

# Exemplo de uso — todos os argumentos devem ser nomeados:
criar_pedido(
    cliente="João da Silva",
    produto="Teclado Mecânico",
    quantidade=2,
    preco_unitario=250.00
)

criar_pedido(
    cliente="Maria Oliveira",
    produto="Monitor 27\"",
    quantidade=1,
    preco_unitario=1300.00,
    forma_pagamento="boleto"
)
