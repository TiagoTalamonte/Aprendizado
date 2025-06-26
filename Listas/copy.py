# Cria uma lista chamada lista1 com os elementos 1, 2 e 3
lista1 = [1, 2, 3]

# Atribui lista1 à lista2 — ambas agora apontam para o MESMO objeto na memória
lista2 = lista1  # NÃO é uma cópia real

# Adiciona o número 4 à lista referenciada por lista2 (que é a mesma de lista1)
lista2.append(4)

# Imprime o conteúdo de lista1 — vai mostrar [1, 2, 3, 4] porque lista1 e lista2 são a mesma lista
print(lista1)  
