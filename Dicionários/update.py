# Adiciona novas chaves e valores.

# Se a chave já existir, atualiza o valor dela.

# Pode receber outro dicionário ou iteráveis de pares chave-valor.

# Dicionário inicial
usuario = {
    'nome': 'Carlos',
    'idade': 30,
    'cidade': 'Rio de Janeiro',
    'hobbies': ['futebol', 'leitura']
}

# Atualizações variadas
novos_dados = {
    'idade': 31,            # Atualiza valor existente
    'profissao': 'Engenheiro'
}

lista_de_tuplas = [
    ('cidade', 'São Paulo'), # Atualiza cidade
    ('email', 'carlos@email.com')
]

# Atualização usando update() com dicionário
usuario.update(novos_dados)

# Atualização usando update() com lista de tuplas
usuario.update(lista_de_tuplas)

# Atualização usando argumentos nomeados
usuario.update(estado='SP', ativo=True)

print(usuario)
