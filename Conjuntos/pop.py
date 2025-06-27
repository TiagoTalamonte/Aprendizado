# Ele remove e retorna um elemento arbitrário do conjunto.

# Como conjuntos não têm ordem, não dá para escolher qual elemento vai ser removido — é sempre um qualquer.

# Se o conjunto estiver vazio, usar pop() gera um erro KeyError.

tarefas = {"lavar louça", "varrer", "limpar janela"}

while tarefas:
    tarefa = tarefas.pop()
    print(f"Executando: {tarefa}")

print("Todas as tarefas foram concluídas.")
