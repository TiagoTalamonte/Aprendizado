nome = "Tiago Talamonte Pintudo de Souza"  
# Define a variável 'nome' com uma string longa

print(nome[0])  
# Imprime o primeiro caractere da string: 'T' (posição 0)

print(nome[-2])  
# Imprime o penúltimo caractere da string: 'z' (índice -2)

print(nome[:9])  
# Imprime do início até o caractere de índice 8 (não inclui o 9): "Tiago Tal"

print(nome[10:])  
# Imprime do caractere de índice 10 até o final: "alamonte Pintudo de Souza"

print(nome[10:16])  
# Imprime do índice 10 até o 15 (não inclui o 16): "alamon"

print(nome[10:16:2])  
# Imprime de 10 até 15, pulando de 2 em 2: "aan"  
# (pega os caracteres de índice 10, 12, 14)

print(nome[:])  
# Imprime a string inteira (mesmo que 'print(nome)')

print(nome[::-1])  
# Inverte a string (do fim para o início): "azuoS ed odutniP etnomalaT ogaiT"
