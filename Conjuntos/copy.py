# Ele cria uma cópia rasa (shallow copy) do conjunto original, ou seja, gera um novo conjunto com os mesmos elementos.

# O novo conjunto é independente do original — modificações em um não afetam o outro.

# Importante para evitar efeitos colaterais ao manipular conjuntos.

conjunto_original = {1, 2, 3}
conjunto_copiado = conjunto_original.copy()

print("Original:", conjunto_original)  # {1, 2, 3}
print("Cópia:", conjunto_copiado)      # {1, 2, 3}

# Modificando o conjunto copiado
conjunto_copiado.add(4)

print("Original após modificação na cópia:", conjunto_original)  
print("Cópia após modificação:", conjunto_copiado)           
