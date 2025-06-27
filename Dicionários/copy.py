# O método copy() em Python cria uma cópia rasa (shallow copy) de um conjunto (set), ou seja, cria um novo conjunto com os mesmos elementos do original, mas que é independente dele.

conjunto_original = {1, 2, 3}
conjunto_copiado = conjunto_original.copy()

print("Original:", conjunto_original)
print("Cópia:", conjunto_copiado)

# Vamos modificar a cópia para ver que o original não muda
conjunto_copiado.add(4)

print("Depois de adicionar 4 na cópia:")
print("Original:", conjunto_original)   
print("Cópia:", conjunto_copiado)       
