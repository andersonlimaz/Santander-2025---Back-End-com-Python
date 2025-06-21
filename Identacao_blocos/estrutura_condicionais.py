MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Maior de idade pode tirar CNH") 

if idade < MAIOR_IDADE:
    print("Menor de idade não pode tirar CNH")

if idade < MAIOR_IDADE:
    print("Menor de idade não pode tirar CNH")
else:
    print("Maior de idade pode tirar CNH")

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar CNH")
elif idade == IDADE_ESPECIAL:
    print("Pode começar aula teóricas, mas não pode aulas praticas")
else:
    print("Ainda não pode tirar a CNH")

    