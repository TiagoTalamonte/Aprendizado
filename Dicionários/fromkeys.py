#fromkeys() é um método de classe usado para criar um dicionário a partir de uma lista (ou outro iterável) de chaves, atribuindo a todas elas o mesmo valor inicial.

# Conjunto de chaves
keys = {'nome', 'idade', 'cidade'}

# Criando dicionário com valor padrão 'desconhecido'
novo_dict = dict.fromkeys(keys, 'desconhecido')

print(novo_dict)
