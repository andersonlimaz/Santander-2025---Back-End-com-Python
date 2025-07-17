n = int(input().strip())

urgentes = []
idosos_normais = []
demais = []

for i in range(n):
    nome, idade, status = input().strip().split(", ")
    idade = int(idade)

    if status == "urgente":
        # Guarda urgentes com idade e nome
        urgentes.append((idade, i, nome))
    elif idade >= 60:
        idosos_normais.append((i, nome))
    else:
        demais.append((i, nome))

# Urgentes por idade decrescente, depois por ordem de chegada
urgentes.sort(key=lambda x: (-x[0], x[1]))
# Idosos normais e demais em ordem de chegada
idosos_normais.sort()
demais.sort()

# Monta ordem final
ordem_atendimento = [nome for _, _, nome in urgentes] + [nome for _, nome in idosos_normais] + [nome for _, nome in demais]

print("Ordem de Atendimento:", ", ".join(ordem_atendimento))
