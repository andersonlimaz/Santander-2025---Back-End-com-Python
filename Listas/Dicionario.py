'''
Criando dicionarios

Um dicionario é um conjunto não-ordenado de pares chave:valor, onde as chaves são unicas em uma dada instância do dicionario.
Dicionarios são delimitados por chaves:{}, e contém uma lista de pares chave: valor separada por vírgulas
'''
pessoa = {"nome":"Anderson", "idade": 28}

pessoa = dict(nome="Anderson", idade=28)

pessoa["telefone"] = "3333-1234" 
print(pessoa)

#Acessando dados do dicionario []

dados = {"nome":"Anderson", "idade": 28, "telefone": "3325-5891"}

dados["nome"]
dados["idade"]
dados["telefone"]
print(dados)

#Sobrescrevendo valor 

dados["nome"] = "Giulia"
dados["idade"] = 29
dados["telefone"] = "9999-5556"
print(dados)

# Dicionários Aninhados
'''
Dicionário podem armazenar qualquer tipo de objeto python como valor, 
desde que a chave para esse valor seja um objeto imutável como (strings e números).
'''
contatos = {
    "andersonlimaz@gmail.com":{"nome":"Anderson", "telefone":"3333-5050"},
    "pedro@gmail.com":{"nome":"pedro", "telefone":"3333-7070"},
    "joao@gmail.com":{"nome":"joao", "telefone":"3333-6060"},
    "ana@gmail.com":{"nome":"ana", "telefone":"3333-5050", "extra":{"a": 1}},
}

telefone = contatos["ana@gmail.com"]["telefone"]
print(telefone)
extra = contatos["ana@gmail.com"]["extra"]["a"]
print(extra)

#iterar 
for chave in contatos:
    print(chave,contatos[chave])

for chave, valor in contatos.items():
    print(chave, valor)

#{}.clear apaga todos valores do dicionario
contatos = {
    "andersonlimaz@gmail.com":{"nome":"Anderson", "telefone":"3333-5050"},
    "pedro@gmail.com":{"nome":"pedro", "telefone":"3333-7070"},
    "joao@gmail.com":{"nome":"joao", "telefone":"3333-6060"},
    "ana@gmail.com":{"nome":"ana", "telefone":"3333-5050", "extra":{"a": 1}},
}
contatos.clear()
print(contatos)

#{}.copy copia 
contatos = {
    "andersonlimaz@gmail.com":{"nome":"Anderson", "telefone":"3333-5050"},
    }
copia = contatos.copy()
copia["andersonlimaz@gmail.com"] = {"nome":"And"}

contatos["andersonlimaz@gmail.com"]

copia = ["andersonlimaz@gmail.com"]

#{}.fromkeys cria dicionario novo usando uma lista de chaves e um valor padrão
dict.fromkeys(["nome", "telefone"])
dict.fromkeys(["nome", "telefone"], "vazio")

# {}.get  acessar o valor de uma chave

contatos = {
    "andersonlimaz@gmail.com":{"nome":"Anderson", "telefone":"3333-5050"},
    }
contatos.get("chave")
contatos.get("chave",{})
contatos.get("andersonlimaz@gmail.com",{})

# {}itens
contatos = {
    "andersonlimaz@gmail.com":{"nome":"Anderson", "telefone":"3333-5050"},
    }
contatos.items()

# {}.keys retorna so a chave
novo_dicionario = {"a":200, 1:"teste","b": "python"}
print(novo_dicionario.keys())

# {}.pop remove um valor do dicionario
contatos = {
    "andersonlimaz@gmail.com":{"nome":"Anderson", "telefone":"3333-5050"},
    }
contatos.pop("andersonlimaz@gmail.com")

contatos.pop("andersonlimaz@gmail.com",{})
print(contatos)

# {}.popitem remove item
contatos = {
    "andersonlimaz@gmail.com":{"nome":"Anderson", "telefone":"3333-5050"},
    }
contatos.popitem() #remove todos itens

# {}setdefault - Esse método serve para buscar uma chave em um dicionário e, se ela não existir, criar essa chave com um valor padrão.
contatos = {"nome":"Anderson", "telefone":"3333-5050"}
    
contatos.setdefault("nome","Giovanna")
print(contatos)
contatos.setdefault("idade",28)
print(contatos)

# {}.update - inserir ou modificar múltiplos pares chave-valor de uma só vez.
contatos = {
    "andersonlimaz@gmail.com":{"nome":"Anderson", "telefone":"3333-5050"},
    }

contatos.update({"andersonlimaz@gmail.com": {"nome":"Gui"}})
contatos # andersonlimaz@gmail.com: {nome: gui}

# {}.values - retorno todos valores da chaves. 
contatos = {
    "andersonlimaz@gmail.com":{"nome":"Anderson", "telefone":"3333-5050"},
    "pedro@gmail.com":{"nome":"pedro", "telefone":"3333-7070"},
    "joao@gmail.com":{"nome":"joao", "telefone":"3333-6060"},
    "ana@gmail.com":{"nome":"ana", "telefone":"3333-5050", "extra":{"a": 1}},
}
contatos.values

# in - de verificação verifica se esta contido

contatos = {
    "andersonlimaz@gmail.com":{"nome":"Anderson", "telefone":"3333-5050"},
    "pedro@gmail.com":{"nome":"pedro", "telefone":"3333-7070"},
    "joao@gmail.com":{"nome":"joao", "telefone":"3333-6060"},
    "ana@gmail.com":{"nome":"ana", "telefone":"3333-5050", "extra":{"a": 1}},
}
"andersonlimaz@gmail.com" in contatos
"anderson@gmail.com" in contatos

# del - retira objetos
contatos = {
    "andersonlimaz@gmail.com":{"nome":"Anderson", "telefone":"3333-5050"},
    "pedro@gmail.com":{"nome":"pedro", "telefone":"3333-7070"},
    "joao@gmail.com":{"nome":"joao", "telefone":"3333-6060"},
    "ana@gmail.com":{"nome":"ana", "telefone":"3333-5050", "extra":{"a": 1}},
}
del contatos["ana@gmail.com"]["telefone"]
del contatos["joao@gmail.com"]
print(contatos)