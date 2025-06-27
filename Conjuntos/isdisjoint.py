# Ele verifica se dois conjuntos não têm elementos em comum — ou seja, se a interseção entre eles é vazia.

# Retorna True se não houver nenhum elemento igual entre os dois conjuntos.

# Retorna False se houver pelo menos um elemento em comum.

grupo_a = {"ana", "bia", "carlos"}
grupo_b = {"daniel", "eduardo", "bia"}

if grupo_a.isdisjoint(grupo_b):
    print("Os grupos não têm membros em comum.")
else:
    print("Os grupos têm membros em comum.")
