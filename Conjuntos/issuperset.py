# Ele verifica se o conjunto que chama o método contém todos os elementos do conjunto passado como argumento.

permissoes_sistema = {"ler", "escrever", "editar", "deletar"}

# Conjunto com permissões que o sistema precisa garantir que inclui certas permissões
permissoes_necessarias = {"ler", "editar"}

# Verificando se o sistema tem todas as permissões necessárias
if permissoes_sistema.issuperset(permissoes_necessarias):
    print("Sistema tem todas as permissões necessárias.")
else:
    print("Sistema não tem todas as permissões necessárias.")
