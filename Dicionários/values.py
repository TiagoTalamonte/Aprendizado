# values() em Python é usado com dicionários para obter uma visão (view) de todos os valores presentes no dicionário.

d = {'nome': 'João', 'idade': 28, 'cidade': 'Belo Horizonte'}

print(d.values())
# Saída: dict_values(['João', 28, 'Belo Horizonte'])

# Podemos iterar nos valores:
for valor in d.values():
    print(valor)
