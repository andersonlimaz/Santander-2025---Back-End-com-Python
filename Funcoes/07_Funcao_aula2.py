def somar(a,b):
    return a + b

def subtrair(a,b):
    return a - b


def exibir_resultado(a,b,funcao):
    resultado = funcao(a,b)
    print(f"O resultado da operação é = {resultado}")

exibir_resultado(10,15,somar)
exibir_resultado(10,10,subtrair)

op, pi = somar, subtrair
print(op(1, 25))
print(pi(1, 3)) 
