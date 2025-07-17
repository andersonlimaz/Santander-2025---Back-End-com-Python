# # Se desconto for 
# produto = input("Informe o produto comprado ? ")
# preco = float(input("Informe o preço ? R$"))
# cupom = input("Informe o cupom? ").strip().upper()

# print(produto,preco,cupom)

# if cupom == "DESCONTO10":
#     preco *= 0.90
#     print(f"Com o DESCONTO10 O VALOR FICOU {preco}")
# elif cupom == "DESCONTO20":
#     preco *= 0.80
#     print(f"Com o DESCONTO10 O VALOR FICOU {preco}")
# else:
#     print(f"Com o DESCONTO10 O VALOR FICOU {preco}")

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
    