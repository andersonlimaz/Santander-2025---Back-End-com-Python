# imprimi os numeros de ordem crescente
for i in range(1,11):
    print(i)
# imprimi os numero de ordem descrecente
for i in range(10, 1, -1):
    print(i)
# Peça um número ao usuário e imprima a tabuada dele (de 1 a 10).
n = int(input("Qual tabuada voce quer calcular? "))
for i in range(1,11):
    resultado = n * i
    print(f"{n}x{i} = {resultado}")

# Mostre todos os números pares entre 0 e 50.
for i in range(1,51):
    if i % 2 ==0:
        print(i)

soma = 0
for i in range(1, 101):
    soma += i
print("Soma:", soma)
