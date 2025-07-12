# Dicionário para agrupar participantes por tema
eventos = {}

# Entrada do número de participantes
n = int(input().strip())

# Loop para armazenar participantes e seus temas
for _ in range(n):
    linha = input().strip()
    nome, tema = linha.split(", ")

    if tema in eventos:
        eventos[tema].append(nome)
    else:
        eventos[tema] = [nome]

# Exibe os grupos organizados
for tema, participantes in eventos.items():
    print(f"{tema}: {', '.join(participantes)}")
