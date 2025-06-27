nome= "Anderson"
idade = 28
profissao = "Programador"
linguagem = "Python"

dados = {"nome": "Guilherme", "idade": 30}

print("nome: %s Idade: %s" % (nome, idade)) #formata a string com %s

print("nome: {} Idade: {}".format (nome, idade)) # formata a string com {}

print("nome: {1} Idade: {0}".format (nome, idade))
print("nome: {1} Idade: {0} Nome: {1} {1}".format (nome, idade))

print("nome: {nome} Idade: {idade} ".format (nome=nome, idade=idade))

print("nome: {nome} Idade: {idade}".format(**dados)) # formata a string com um dicionário

print(f"nome: {nome} Idade: {idade}") # formata a string com f-strings (Python 3.6+)