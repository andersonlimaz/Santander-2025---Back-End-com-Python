'''
Nosso primeiro programa POO

João tem uma bicibletaria e gostaria de registaria as vendas de suas bicicletas. Crie um programa onde João informe: 
cor, modelo, ano e valor da bicicleta vendida. Um bicicleta pode: buzinar, parar e correr. Adicione esses comportamentos.
'''
class bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("PEEE PEEE")

    def parar(self):
        print("parando bicicleta")
        print("bicicleta parada!")
    
    def correr(self):
        print("Vaaaappp...")

    def __str__(self):
        return f"{self.__class__.__name__}:{', '.join([f'{chave}={valor}' for chave,valor in self.__dict__.items()])}"
# b1 = bicicleta("azul","caloi","2010","2000")
# b1.buzinar()
# b1.correr()
# b1.parar()
# print(b1.cor, b1.modelo, b1.ano, b1.valor)


b2 = bicicleta("verde","Ronaldo",2003,190)
bicicleta.buzinar() 