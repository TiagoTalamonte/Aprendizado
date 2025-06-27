# Conjunto de frutas disponíveis no estoque
estoque = {"maçã", "banana", "laranja", "abacaxi", "uva"}

# Conjunto de frutas que o cliente deseja
pedido_cliente = {"banana", "kiwi", "uva", "pera"}

# Verificando o que tem ou não tem no estoque
for fruta in pedido_cliente:
    if fruta in estoque:
        print(f" Temos {fruta} em estoque.")
    else:
        print(f" Não temos {fruta} no momento.")
