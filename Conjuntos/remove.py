# Ele remove um elemento específico do conjunto.

# Se o elemento não estiver presente no conjunto, o método gera um erro KeyError.

# Ao contrário do discard(), que não gera erro se o elemento não existir.

usuarios = {"ana", "bia", "carlos"}

usuario_para_remover = "daniel"

if usuario_para_remover in usuarios:
    usuarios.remove(usuario_para_remover)
else:
    print(f"Usuário {usuario_para_remover} não encontrado.")

print(usuarios)  
