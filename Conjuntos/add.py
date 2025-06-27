# Ele adiciona um elemento ao conjunto, se ele ainda não existir.

# Como conjunto não aceita elementos duplicados, se você adicionar um valor que já está lá, nada muda.

# O conjunto é mutável, ou seja, o próprio conjunto é modificado.

usuarios_ativos = {"ana", "bia", "carlos"}

# Novo usuário entra no sistema
novo_usuario = "daniel"
usuarios_ativos.add(novo_usuario)

# Tentar adicionar um usuário que já está ativo
usuarios_ativos.add("bia")

print(usuarios_ativos)  

