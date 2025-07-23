# Construtores e Destrutors
'''
Metodo construtor ou inicializador sempre é executado quando uma nova instância da classe é criada. Nesse método inicializamos o estado
do nosso objeto. Para declarar o método construtor da classe, criamos um método com o nome __init__.
'''

# class cachorro:
#     def __init__(self, nome, cor, acordado=True):
#         self.nome = nome
#         self.corcor = cor
#         self.acordado = acordado
        
# Método destrutor
'''
O método destruor sempre é executado quando uma instância (objeto) é destruida. 
Destrutores em Python não são tão necessarios quanto em c++ porque o python tem um coletor de lixo que lida com o gerenciamento 
de memoria automaticamente. Para declarar o método destrutor da classe, criamos um método com o nome __del__.
'''
# class cachorro:
#     def __del__(self):
#         print("Destruindo a instacia")

# c = cachorro()
# del c

# Exemplo
class cachorro:
    def __init__(self,nome,cor,acordado=True):
        print("inicializando a classe...")
    
        self.nome = nome
        self.cor = cor
        self.acordado = acordado  

    def __del__(self):
        print("Removendo a instância da classe")

    def falar(self):
        print("Auau")

def criar_cachorro():
    c= cachorro("Zeus","branco e preto", False)
    print(c.nome)

c = cachorro("Lobo", "roxo")
c.falar() 

print("Olá mundo")
print("Olá mundo")
del c
print("Olá mundo")
print("Olá mundo")
print("Olá mundo")