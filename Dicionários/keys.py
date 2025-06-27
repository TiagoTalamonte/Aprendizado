#keys() em Python é usado com dicionários para obter uma visão (view) de todas as chaves presentes no dicionário.

d = {'nome': 'Maria', 'idade': 25, 'cidade': 'Rio de Janeiro'}

print(d.keys())
# Saída: dict_keys(['nome', 'idade', 'cidade'])

# Podemos iterar nas chaves:
for chave in d.keys():
    print(chave)
