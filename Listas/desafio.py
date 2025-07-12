# Lista para armazenar os produtos e preços
carrinho = []

# Variável para armazenar o total
total = 0.0

# Entrada do número de itens
n = int(input().strip())

# Loop para adicionar os itens ao carrinho
for _ in range(n):
    linha = input().strip()

    # Encontrar a última ocorrência de espaço para separar nome e preço
    pos = linha.rfind(" ")

    # Separar nome do produto e o preço
    nome = linha[:pos]
    preco = float(linha[pos + 1:])

    # Adicionar ao carrinho e somar ao total
    carrinho.append((nome, preco))
    total += preco

# Imprimir os produtos
for nome, preco in carrinho:
    print(f"{nome}: R${preco:.2f}")

# Imprimir o total
print(f"Total: R${total:.2f}")
