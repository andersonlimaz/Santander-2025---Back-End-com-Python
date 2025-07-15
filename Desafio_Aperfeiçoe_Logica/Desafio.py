# Entrada
preco = float(input())
cupom = input().strip().upper()

# Aplicação das regras de desconto
if cupom == "DESCONTO10":
    preco_final = preco * 0.90
    print(f"{preco_final:.2f}")
elif cupom == "DESCONTO20":
    preco_final = preco * 0.80
    print(f"{preco_final:.2f}")
elif cupom == "SEM_DESCONTO":
    print(f"{preco:.2f}")
else:
    print("Cupom inválido")
    