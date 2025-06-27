# intersection() retorna um novo conjunto com somente os elementos que existem nos dois conjuntos.

# Ideal para encontrar interesses comuns, participações conjuntas, etc.

# Também pode ser usado com mais de dois conjuntos, como:

# Alunos que fizeram a Prova 1
prova1 = {"Ana", "Bruno", "Carlos", "Diana", "Eduardo"}

# Alunos que fizeram a Prova 2
prova2 = {"Carlos", "Diana", "Fernanda", "Gustavo", "Ana"}

# Interseção: alunos que fizeram as duas provas
fez_ambas = prova1.intersection(prova2)

print("Alunos que fizeram as duas provas:")
for aluno in sorted(fez_ambas):
    print(f"- {aluno}")
