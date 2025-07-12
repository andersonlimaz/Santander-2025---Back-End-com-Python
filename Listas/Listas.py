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
print(lista[2:])# p, y 
print(lista[:2]) #hon
print(lista[1:3])#p t
print(lista[0:3:2])#p, t
print(lista[::]) #python
print(lista[::-1])#nohtyp

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

#Método [].append adiciona valores na lista
lista = []

lista.append(1)
lista.append("python")
lista.append([40,30,20])

print(lista)

# [].clear Limpa valores da lista
lista = [1,"python",[40,30,20]]

print(lista)

lista.clear()
print(list)

# [].copy copia valores da lista
lista = [1,"python",[40,30,20]]

l2 = lista.copy()
print(lista)

print(id(l2), id(lista))
l2[0] = 2
print(l2)
print(lista)

# [].count conta quantidade de vezes que valor aparece na lista
cores = ["vermelho", "azul", "verde", "azul"]

print(cores.count("vermelho"))
print(cores.count("azul"))
print(cores.count("verde"))

# [].extend junta duas listas
linguagens = ["python","js","c"]
print(linguagens)

linguagens.extend(["java","csharp"])
print(linguagens)

# [].index mostra o indice da palavra produrada
linguagens = ["python","js","c","java","csharp"]

print(linguagens.index("java"))
print(linguagens.index("python"))

# [].pop tira o ultimo elemento da lista, ou pode usar para remover item da lista
linguagens = ["python","js","c","java","csharp"]
print(linguagens.pop())
print(linguagens.pop())
print(linguagens.pop())
print(linguagens.pop(0))

# [].remove, remove valor especiicado.
linguagens = ["python","js","c","java","csharp"]
linguagens.remove("c")
linguagens.remove("java")

print(linguagens)

# .reverse espelha lista 
linguagens = ["python","js","c","java","csharp"]
linguagens.reverse()

print(linguagens)

# [].sort ordena lista por ordem alfabetica
linguagens = ["python","js","c","java","csharp"]
linguagens.sort() 

linguagens = ["python","js","c","java","csharp"]
linguagens.sort(reverse=True) 

linguagens = ["python","js","c","java","csharp"]
linguagens.sort(key=lambda x: len(x)) 

linguagens = ["python","js","c","java","csharp"]
linguagens.sort(key=lambda x: len(x), reverse=True) 

# len = usa para ver o tamanho da lista.
linguagens = ["python","js","c","java","csharp"]
len(linguagens)

# sorted ordena interaveis mesma coisa de sort mudando que ele é uma função

linguagens = ["python","js","c","java","csharp"]
linguagens.sort(key=lambda x: len(x)) 

linguagens = ["python","js","c","java","csharp"]
sorted(linguagens, key=lambda x: len(x))
sorted(linguagens, key=lambda x: len(x), reverse=True)
