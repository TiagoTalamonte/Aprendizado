# método setdefault() em Python é usado em dicionários para:

# Buscar o valor de uma chave.

# Se a chave não existir, adiciona essa chave ao dicionário com um valor padrão que você define (ou None se não definir) e retorna esse valor.

dados = {'nome': 'Ana', 'idade': 25}

# Busca a chave 'cidade'. Como não existe, adiciona com valor 'São Paulo'
cidade = dados.setdefault('cidade', 'São Paulo')

print(cidade)       # Saída: São Paulo
print(dados)
# Saída: {'nome': 'Ana', 'idade': 25, 'cidade': 'São Paulo'}

# Se chamar de novo, não altera porque já existe a chave
cidade2 = dados.setdefault('cidade', 'Rio de Janeiro')
print(cidade2)      # Saída: São Paulo
