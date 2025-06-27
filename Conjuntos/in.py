# Ele verifica se um valor existe dentro de uma coleção (como conjunto, lista, tupla, dicionário).

# Retorna True se o elemento está presente.

# Retorna False se não está.

usuarios_ativos = {"ana", "bia", "carlos"}

usuario = "bia"

if usuario in usuarios_ativos:
    print(f"{usuario} está ativo.")
else:
    print(f"{usuario} não está ativo.")
