# Conceito de classes e objetos

#Classe
'''
Uma classe define as características e comportamentos de um objeto, porém não conseguimos usá-las diretamente.
Ja os objetos podemos usa-los e eles possuem as caracteristicas e comportamentos que foram definidos nas classes. 


💡 Classe é como a receita de bolo. Ela diz os ingredientes (dados) e o modo de preparo (ações) — mas não é o bolo em si.
🎂 Objeto é o bolo pronto feito a partir daquela receita. 
Você pode fazer vários bolos com a mesma receita, cada um com variações pequenas (como cobertura diferente, por exemplo)
'''
#Classe
class cachorro:
    def __init__(self, nome, cor, acordado=True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
        
    def latir(self):
        print("Auau")
    def dormir(self):
        self.acordado = False
        print("Zzzzz")

# Objeto
cao_1 = cachorro("Lobo","Marrom", False)
cao_2 = cachorro("Caramelo", "Caramelo",)

cao_1.latir()

print(cao_2.acordado)
cao_2.dormir()
print(cao_2.acordado)