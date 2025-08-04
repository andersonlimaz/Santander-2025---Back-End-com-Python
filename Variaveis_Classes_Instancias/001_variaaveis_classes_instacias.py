'''
Atributos do objeto

todos os objetos nascem com o mesmo número de atributos de classe e de instância.
Atributos de instância são diferentes para cada objeto (Cada objeto tem uma cópia), 
ja os atributos de classe são compartilhados entre os objetos
'''
class Estudante:
    escola = "Dio"

    def __init__(self,nome, matricula):
        self.nome = nome
        self.matricula = matricula
    
    def __str__(self):
        return f"{self.nome} ({self.matricula}) - {self.escola} "
    
def mostrar_valores(*objs):
    for obj in objs:
        print(obj)
    
aluno1 = Estudante("Anderson", 1,)
aluno2 = Estudante("Giulia", 2)
mostrar_valores(aluno1,aluno2)


Estudante.escola = "Ingles"
aluno3 = Estudante("Ronaldo", 3)
mostrar_valores(aluno1,aluno2,aluno3)