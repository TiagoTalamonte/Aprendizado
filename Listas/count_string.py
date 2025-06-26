# Define uma string com uma frase
frase = "A linguagem Python é poderosa. Python é popular."

# Conta quantas vezes a palavra "Python" aparece na frase
quantidade_python = frase.count("Python")  # Deve retornar 2

# Conta quantas vezes a letra "o" aparece na frase
quantidade_o = frase.count("o")  # Deve retornar 4 (conta cada letra 'o')

# Conta quantas vezes a palavra "Java" aparece na frase (não existe)
quantidade_java = frase.count("Java")  # Deve retornar 0

# Imprime os resultados
print("A palavra 'Python' aparece:", quantidade_python, "vezes")  
print("A letra 'o' aparece:", quantidade_o, "vezes")              
print("A palavra 'Java' aparece:", quantidade_java, "vezes")      
