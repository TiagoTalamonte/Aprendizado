# Ele remove todos os elementos do conjunto, deixando-o vazio.

# O conjunto permanece criado, mas sem nenhum item dentro.

# É um método que modifica o conjunto original.

usuarios_conectados = {"ana", "bia", "carlos"}

print(f"Usuários antes da reinicialização: {usuarios_conectados}")

# Reinicia sistema, limpar todos os usuários conectados
usuarios_conectados.clear()

print(f"Usuários após reinicialização: {usuarios_conectados}")
