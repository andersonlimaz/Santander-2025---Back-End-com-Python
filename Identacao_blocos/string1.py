curso ="pYThon"


print(curso.upper())  # Converte a string para maiúsculas
print(curso.lower())  # Converte a string para minúsculas
print(curso.title()) #Converte a string para título (primeira letra de cada palavra em maiúscula)
print(curso.capitalize()) #converte a primeira letra da string para maiúscula

nome =    "Hello Word!"

print(nome.strip()) # remove espaços em branco no inicio 
print(nome.lstrip()) # remove espaços em branco no inicio
print(nome.rstrip()) # remove espaços em branco no final


print(nome.center(10,'$')) # centraliza a string em um campo de 10 caracteres, preenchendo com '$'
print(".".join(curso)) # junta os caracteres da string com '.'
print(nome.replace("Hello", "Olá")) # substitui "Hello" por "Olá"
print(nome.split()) # divide a string em uma lista de palavras

menu = "Corinthians"
print("###" + menu + "###") # adiciona '###' antes e depois da string
print(menu.center(14))  # centraliza a string em um campo de 14 caracteres, preenchendo com espaços
print(menu.center(14, '#')) # centraliza a string em um campo de 14 caracteres, preenchendo com '#'
print("-".join(menu)) # junta os caracteres da string com '-'

