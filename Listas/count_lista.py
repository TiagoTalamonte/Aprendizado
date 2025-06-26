# Cria uma lista de frutas com algumas repetidas
frutas = ["maçã", "banana", "maçã", "laranja", "banana", "maçã", "uva"]

# Conta quantas vezes a fruta "maçã" aparece na lista
quantidade_maca = frutas.count("maçã")  # Deve retornar 3

# Conta quantas vezes a fruta "banana" aparece na lista
quantidade_banana = frutas.count("banana")  # Deve retornar 2

# Conta quantas vezes a fruta "melancia" aparece (não está na lista)
quantidade_melancia = frutas.count("melancia")  # Deve retornar 0

# Imprime os resultados
print("Maçã aparece:", quantidade_maca, "vezes")        
print("Banana aparece:", quantidade_banana, "vezes")    
print("Melancia aparece:", quantidade_melancia, "vezes")  
