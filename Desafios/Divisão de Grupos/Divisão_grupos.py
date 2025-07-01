# Lê o número de participantes
n = int(input().strip())

# Dicionário para agrupar participantes por tema
eventos = {}

# Loop para ler os participantes e seus temas
for _ in range(n):
    linha = input().strip()
    participante, tema = linha.split(", ")
    if tema not in eventos:
        eventos[tema] = []
    eventos[tema].append(participante)

# Imprime os grupos organizados no formato desejado
for tema, participantes in eventos.items():
    print(f"{tema}: {', '.join(participantes)}")
