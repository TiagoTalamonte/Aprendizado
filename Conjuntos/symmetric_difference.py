# symmetric_difference() retorna os elementos que não estão em ambos os conjuntos ao mesmo tempo.

# Em outras palavras: (A ∪ B) - (A ∩ B).

# Também pode ser feito com o operador ^:

# Alunos que fizeram a Prova 1
prova1 = {"Ana", "Bruno", "Carlos", "Diana", "Eduardo"}

# Alunos que fizeram a Prova 2
prova2 = {"Carlos", "Diana", "Fernanda", "Gustavo", "Ana"}

# Diferença simétrica: quem fez só uma das provas
so_uma_prova = prova1.symmetric_difference(prova2)

print("Alunos que fizeram apenas uma das provas:")
for aluno in sorted(so_uma_prova):
    print(f"- {aluno}")
