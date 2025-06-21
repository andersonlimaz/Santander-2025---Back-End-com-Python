
while True:
    numero = int(input("informe um numero? "))

    if numero == 10:
        break # encerra o laço quando o numero for 10
    print(numero)

for numero in range(101):

    if numero == 12:
        continue # pula o numero 12

    print(numero, end=" ")