# Método de classe 
'''
Métodos de classe estão ligados á classe e não ao objeto. 
Eles têm acesso ao estado da classe, pois recebem um parâmetro que aponta para a classe e não para a intância do objeto

Métodos estáticos

Um método estático não recebe um primeiro argumento explícito. Ele também é um método vinculado á classe e não ao objeto da classe.
Este método não pode acessar ou modificar o estado da classe. Ele está presente em uma classe porque faz sentido que o método esteja
presente na classe. 

Métodos de classe x Métodos estáticos

Um método de classe recebe um primeiro parâmetro que aponta para a classe, 
enquanto um método ou modificar o estado da classe enquanto um método estático não pode acessá-lo ou modificá-lo.

Quanto utilizar método de classe ou estático

Geralente usamos o método de classe para criar métodos de fabrica.
Geralmente usamos métodos estáticos para criar funções utilitarias
'''

class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade
    
    @classmethod
    def criar_data_nasc(cls, ano, mes, dia, nome):
        print(cls)
        idade = 2025 - ano
        return cls(nome, idade)
    
    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18

    
# x=Pessoa("Anderson",28)
# print(x.nome,x.idade)

p = Pessoa.criar_data_nasc(1996,10,2,"Anderson")
print(p.nome,p.idade)

print(Pessoa.e_maior_idade(18))
print(Pessoa.e_maior_idade(8))