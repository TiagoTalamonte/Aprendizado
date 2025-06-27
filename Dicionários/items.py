# items() em Python é usado com dicionários para retornar uma visão (view) dos pares (chave, valor) do dicionário.

d = {'nome': 'Ana', 'idade': 30, 'cidade': 'São Paulo'}

for chave, valor in d.items():
    print(f'{chave}: {valor}')
