
def calcular_total(numeros):
    return sum(numeros)
    
def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1
    return antecessor,sucessor

def raiz_quadrada(numero):
    numero = numero * numero
    print(f"A raiz quadrada desse numero é {numero}")

def func_3():
    print("Olá mundo!")
    

print(calcular_total([10,20,34]))    
print(retorna_antecessor_e_sucessor(10))
raiz_quadrada(17)
print(func_3()) #Quando não passa argumento o retorno é none