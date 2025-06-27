#método popitem() em Python é usado com dicionários para remover e retornar um par (chave, valor) arbitrário do dicionário.

d = {'a': 1, 'b': 2, 'c': 3}

item = d.popitem()
print("Item removido:", item)  # Exemplo: ('c', 3)
print("Dicionário agora:", d)  # {'a': 1, 'b': 2}
