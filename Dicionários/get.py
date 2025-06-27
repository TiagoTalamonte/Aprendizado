# get() é usado em dicionários para acessar o valor de uma chave, mas de forma segura, evitando erro caso a chave não exista.

dados = {'nome': 'Tiago', 'idade': 27}

print(dados.get('nome'))       # Saída: Tiago
print(dados.get('cidade'))     # Saída: None (pois não existe a chave 'cidade')
print(dados.get('cidade', 'Não informado'))  