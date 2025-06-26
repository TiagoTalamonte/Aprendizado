nome = "Tiago"  # Define a variável 'nome' com a string "Tiago"
idade = 27  # Define a variável 'idade' com o número inteiro 27
profissao = "Idiota"  # Define a variável 'profissao' com a string "Idiota"
Linguagem = "Python"  # Define a variável 'Linguagem' com a string "Python"
saldo = 500.000  # Define a variável 'saldo' com o valor float 500000.0 (ponto decimal)

dados = {"nome": "Tiago", "idade": 27}  # Define um dicionário com as chaves 'nome' e 'idade'

# Formatação antiga de string (operador %):
print("Nome: %s idade: %d" % (nome, idade))  
# %s para string, %d para inteiro; substitui os valores na ordem dos parênteses

# Formatação usando método format padrão:
print("Nome: {} idade: {}".format(nome, idade))  
# Coloca as variáveis na ordem das chaves vazias {}

# Formatação com indices invertidos dentro do format:
print("Nome: {1} idade: {0}".format(idade, nome))  
# {1} pega o segundo argumento (nome), {0} o primeiro (idade)

# Repetindo a mesma variável várias vezes na string formatada:
print("Nome: {1} idade: {0} Nome: {1} {1}".format(idade, nome))  
# Imprime nome e idade, depois repete o nome três vezes

# Usando nomes de variáveis dentro do format:
print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade))  
# Substitui pelas variáveis nome e idade explicitamente nomeadas

# Usando nomes diferentes para as variáveis no format:
print("Nome: {name} Idade: {age}".format(age=idade, name=nome))  
# Usa nome 'name' e 'age' no lugar das variáveis para o format

# Usando o dicionário e desempacotando com ** para formatar:
print("Nome: {nome} Idade: {idade}".format(**dados))  
# Passa as chaves do dicionário como argumentos nomeados para o format

# Usando f-string para interpolação direta (Python 3.6+):
print(f"Nome: {nome} Idade: {idade}")  
# Insere as variáveis diretamente dentro da string com {}

# F-string formatando saldo com largura 10 e 3 casas decimais:
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:10.3f}")  
# :10.3f significa campo com 10 caracteres, float com 3 decimais

# F-string formatando saldo com 3 casas decimais (sem largura fixa):
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.3f}")  
# :.3f significa float com 3 casas decimais, campo ajustável
