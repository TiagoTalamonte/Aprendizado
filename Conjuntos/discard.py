# Ele remove um elemento específico do conjunto, se ele existir.

# Se o elemento não estiver no conjunto, o método não gera erro — simplesmente não faz nada.

# É diferente do remove(), que lança um erro se o elemento não existir.

usuarios = {"ana", "bia", "carlos"}

usuarios.discard("bia")    # Remove 'bia'
usuarios.discard("daniel") # 'daniel' não está no conjunto, mas não gera erro

print(usuarios)  
