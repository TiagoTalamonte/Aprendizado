# difference() compara dois conjuntos e retorna os elementos que estão no primeiro, mas não no segundo.

# A operação não é simétrica, ou seja:

# Alunos que fizeram a Prova 1
prova1 = {"Ana", "Bruno", "Carlos", "Diana", "Eduardo"}

# Alunos que fizeram a Prova 2
prova2 = {"Carlos", "Diana", "Fernanda", "Gustavo", "Ana"}

# Diferença: alunos que fizeram somente a Prova 1
somente_prova1 = prova1.difference(prova2)

print("Alunos que fizeram apenas a Prova 1:")
for aluno in sorted(somente_prova1):
    print(f"- {aluno}")
