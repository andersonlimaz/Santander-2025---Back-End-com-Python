'''O que é polimorfismo?
A palavras polimorfismo significa ter muitas formas. Na programação, 
polimorfismo significa o mesmo nome de função (mas assinaturas diferentes) sendo usado para tipos diferentes. 



Mesmo método com comportamento diferente. 
Na herança, a classe filha herda os métodos da classe pai. No entanto, 
é possível modificar um método em uma classe filha herdada da classe pai. 
Isso é particularmente útil nos casos em que o método herdado da classe pai não se encaixa perfeitamente na classe filha.
'''
class Passaro:
    def voar(self):
        print("Voando ...")

class Pardal(Passaro):
    def voar(self):
     return super().voar()
    
class Avestruz(Passaro):
   def voar(self):
      print("Avestruz não pode voar")

# FIXME: exemplo ruim do uso de henrança para "Ganhar" o metodo voar
class Aviao(Passaro):
   def voar(self):
      print("aviao esta decolando...")

def plano_voo(obj):
   obj.voar()

p1 = Pardal()
p2 = Avestruz()
p3 = Aviao()

plano_voo(p1)
plano_voo(p2)
plano_voo(p3)