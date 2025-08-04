# O que são interfaces

'''
Em Python, interfaces são uma forma de definir um "contrato" que uma classe deve seguir — 
ou seja, um conjunto de métodos que precisam ser implementados. 
Embora Python não tenha uma palavra-chave interface como Java ou C#, 
ele oferece formas de criar esse comportamento usando classes abstratas.

Interfaces definem o que uma classe deve fazer e não como.

Python tem interface?

O conceito de interface é definir um contrato, onde são declarados os métodos
(o que deve ser feito) e suas respectivas assinaturas. Em python utilizamos classe
abstratasa para criar contratos. Classes abstratas não podem ser instanciadas. 


Abc 

por padrão, o Python não fornece classes abstratas. 
O Python vem com um módulo que fornece a base para definir as classes abstratas, 
e o nome do módulo é ABC. O ABC funciona decorando métodos da classe base como abstratos e, 
em seguida, registrando classe concretas como implementações da base abstrata. 
Um método se torna abstrato quando decorado com @abstractmethod. 
'''
from abc import ABC, abstractmethod, abstractproperty


class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractproperty
    def marca(self):
        pass

class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando TV")
        print("Ligado!")
    
    def desligar(self):
        print("Desligando a TV...")
        print("Desligado!")

    @property
    def marca(self):
        return "Samsung"

class ContreleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando Ar Condicionado")
        print("Ligado!")
    
    def desligar(self):
        print("Desligando Ar Condicionado...")
        print("Desligado!")

    @property
    def marca(self):
        return "york"

controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)

controle = ContreleArCondicionado()
controle.ligar()
controle.desligar()
print(controle.marca)
