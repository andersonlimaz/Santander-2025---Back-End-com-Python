'''
O que são Funções ?
Funções é um bloco de codigo identificado por um nome e pode receber uma lista de parametros.
esses parâmetros podem ou não ter padroes. Usar funções torna o código mais legivel e possibilita o reaproveitamento de códigos.
Programar baseado em funções, é o mesmo que dizer que estamos programando de maneira estruturada.
'''
def exibir_nome():
    print("Hello Word!")
def exibir_nome_1(nome):
    print(f"Seja bem vindo {nome}!")
def exibir_nome_2(nome="Anonimo",vindo="vindo(a)"):
    print(f"Seja bem {vindo} {nome}!")

exibir_nome()
exibir_nome_1(nome="Anderson")
exibir_nome_2()
exibir_nome_2(nome="Anderson")
