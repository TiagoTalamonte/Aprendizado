#Ele retorna um conjunto que é a união de dois ou mais conjuntos, ou seja, todos os elementos que estão em pelo menos um dos conjuntos.

# Conjunto de convidados do Evento A
convidados_evento_a = {"Ana", "Carlos", "João", "Maria"}

# Conjunto de convidados do Evento B
convidados_evento_b = {"João", "Fernanda", "Miguel", "Ana"}

# Unindo os conjuntos com union()
convidados_gerais = convidados_evento_a.union(convidados_evento_b)

# Exibindo todos os convidados únicos dos dois eventos
print("Lista final de convidados:")
for nome in sorted(convidados_gerais):
    print(f"- {nome}")
