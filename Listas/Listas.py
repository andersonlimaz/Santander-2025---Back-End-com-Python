frutas = ["laranja","pera","maca"]
print(frutas)

frutas = []
print(frutas)

letras = list("python")
print(letras)

numeros = list(range(10))
print(numeros)

carro = ["ferrari", "F8", 422256, 2025, 2900, "São Paulo", True ]
print(carro)

#Acesso de Valores 
'''
A lista é uma sequencia, portanto podemos acessar seus dados utilizando índices. contamos o indice de determinada sequência a partir do zero.
'''
frutas = ["pera","maca","abacaxi","morango"]
frutas[0]
frutas[2]

#Indices Negativos
'''
Sequência suportam indexação negativa. A contagem começa em -1. 
'''
frutas = ["pera","maca","abacaxi","morango"]
frutas[-1]# O indice de numeros negativos começa no -1
frutas[-3]

#Lista aninhadas
'''
listas podem armazenar todos os tipos de objetos em python, portanto podemos ter listas que armazenam outras listas
Com isso podemos podemos criar estrutaturas bidimencionais (tabelas), e acessar informando os indices de linha e coluna.
'''
matriz = [
    [1,"a",2],
    ["b", 3, 4],
    [6, 5, "c"]
]
matriz[0]# [1,a,2]
matriz[0][0] # [1]
matriz[0][-1]# [2]
matriz[-1][-1]#["c"]
matriz[2][1] #["5"]

#Fatiamento
lista= ["p","y","t","h","o","n"]
lista[2:]
lista[:2]
lista[1:3]
lista[0:3:2]
lista[::]
lista[::-1]

carros = ["gol", "celta","palio",]

for carro in carros:
    print(carro)
    
carros= ["gol","celta","palio"]
for indice, carro in enumerate(carros):
    print(f"{indice}:{carro}")

numeros = [ 1, 30, 21, 2 ,3 ,8]
pares = []
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
        print(numeros, pares)

numeros = [ 1, 30, 21, 2 ,3 ,8]
pares = [numero for numero in numeros if numero % 2 == 0]

numeros = [ 1, 30, 21, 2 ,3 ,8]
quadrado = []
for numero in numeros:
    quadrado.append(numero ** 2 )
     