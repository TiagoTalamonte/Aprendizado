# issubset() verifica se todos os elementos do conjunto chamado (aqui conjunto1) estão presentes no conjunto passado como argumento (conjunto2).

# No exemplo, todos os elementos de conjunto1 estão em conjunto2, então retorna True.

permissoes_sistema = {"ler", "escrever", "editar", "deletar"}

# Permissões concedidas a um usuário
permissoes_usuario1 = {"ler", "escrever"}
permissoes_usuario2 = {"ler", "editar", "executar"}  # 'executar' não está no sistema

# Função para validar se as permissões do usuário são válidas (estão dentro das permissões do sistema)
def validar_permissoes(permissoes_usuario, permissoes_sistema):
    if permissoes_usuario.issubset(permissoes_sistema):
        return "Permissões válidas."
    else:
        # Encontrar permissões inválidas
        invalidas = permissoes_usuario.difference(permissoes_sistema)
        return f"Permissões inválidas detectadas: {invalidas}"

# Testando
print(validar_permissoes(permissoes_usuario1, permissoes_sistema))  # Permissões válidas.
print(validar_permissoes(permissoes_usuario2, permissoes_sistema))  # Permissões inválidas detectadas: {'executar'}

# Outro exemplo: verificando se uma palavra é subconjunto de letras permitidas
letras_permitidas = set("abcdefghijklmnopqrstuvwxyz")

palavra1 = set("python")
palavra2 = set("Python3")

print(palavra1.issubset(letras_permitidas))  
print(palavra2.issubset(letras_permitidas))  