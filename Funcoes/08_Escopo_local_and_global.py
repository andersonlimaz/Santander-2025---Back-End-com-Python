'''
Escopo local e escopo global
python trabalha com escopo local e global, dentro do bloco da função o escopo é local.
Portanto alterações ali feitas em objetos imutaveis serão perdidas quando o método terminar
de ser executado. Para usar objetos globais utilizamos a palavra-chave global, que informa ao interpretador que 
a variável que esta sendo manipulada no escopo local é global. Essa Não é uma pratica e deve ser evitada. 
'''
salario = 2000
def salario_bonus(bonus):
    
    lista_aux = lista.copy()
    lista_aux.append(2)
    print(f"lista aux={lista_aux}")


    global salario
    salario += bonus
    return salario

lista = [1]
salario_com_bonus = salario_bonus(500)
print(salario_com_bonus)
print(lista)