'''
Tuplas são estruturas de dados muito parecidas com as listas, a principal diferença é que tupla são mutaveis enquanto listas são mutáveis.
Podemos criar tuplas através da classe tuple, ou colocando valores separdos por vígula de parenteses
'''
frutas = ("laranja", "pera", "uva",)
letras = tuple("python")

numeros = tuple([1,2,3,4])
pais = ("Brasil",)

# tuplas Aninhadas
matriz = (
    (1,"a",2),
    ("b", 3, 4),
    (6, 5, "c"),
)
matriz[0]# [1,a,2]
matriz[0][0] # [1]
matriz[0][-1]# [2]
matriz[-1][-1]#["c"]

# tuplas conta com menos metodos, len count e index. 

carros = ("gol") 
print(isinstance(carros, tuple))