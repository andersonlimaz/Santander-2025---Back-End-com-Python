'''
Conjuntos: criando sets

Um set é uma coleção que não possui objetos repetidos, 
usamos sets para repesentar conjuntos matematicos ou eliminar itens duplicados de um iterável. 
'''

# set Elimina valores iguais,trazendo uma ordem é aleatoria. 

set([1,2,3,1,3,4,4]) #{1,2,3,4}
set("abacaxi") #{"b","a","c","x","i"}
set(("palio","gol","celta","palio"))#`{"gol","celta","palio"}`

#convertente set em lista
numeros = {1,2,3,4}
numeros = list(numeros)
numeros[0]

# union une os dois conjuntos
conjunto_a = {1,2,3}
conjunto_b = {2,3,4}

conjunto_a.union(conjunto_b) #{1,2,3,4}

# intersection pega valores iguais
conjunto_a = {1,2,3}
conjunto_b = {2,3,4}

conjunto_a.intersection(conjunto_b) # {2,3}

# difference - pega a diferença entre dois conjuntos
conjunto_a = {1,2,3}
conjunto_b = {2,3,4}

conjunto_a.difference(conjunto_b) # {1}
conjunto_b.difference(conjunto_a) # {4}

# symmetric_difference - pega total diferença entre a e b
conjunto_a = {1,2,3}
conjunto_b = {2,3,4}

conjunto_a.symmetric_difference(conjunto_b) #{1,4}