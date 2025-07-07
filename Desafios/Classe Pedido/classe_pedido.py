class Pedido:
    def __init__(self):
        self.itens = []  
    
    # Método para adicionar um item ao pedido
    def adicionar_item(self, preco):
        # Adiciona o preço do item à lista
        self.itens.append(preco)

    # Método para calcular o total do pedido
    def calcular_total(self):
        # Retorna a soma de todos os preços
        return sum(self.itens)


# Lê a quantidade de pedidos
quantidade_pedidos = int(input().strip())

pedido = Pedido()

for _ in range(quantidade_pedidos):
    entrada = input().strip()
    nome, preco = entrada.rsplit(" ", 1)  # Separa o nome do preço (última parte)
    preco = float(preco)
    # Chama o método adicionar_item corretamente
    pedido.adicionar_item(preco)

# Exibe o total formatado com duas casas decimais
print(f"{pedido.calcular_total():.2f}")
