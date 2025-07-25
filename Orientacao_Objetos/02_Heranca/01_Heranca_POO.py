# Herança 
'''
Em programação herença é a capacidade de uma classe filha derivar ou herdar caracteristicas e comportamentos da classe pai (Base)
'''
# Beneficios da herança
'''
ºRepresenta bem os relacionamentos do mundo real.
ºFornece reutilização de código, não precisamos escrever o mesmo código repetidamente, Além disso, permite adicionar mais recursos a uma classe sem modificá-la
ºÉ de natureza transitiva, o que significa que, se a classe B herdar da classe A, todas as subclasses de B herdarão automaticamente da classe A. 
'''
# herança simple
'''
Quando uma classe filha herda apenas uma classe pai, ela é chamada de herança simples. 
'''
class A:
    pass
class B(A):
    pass

# Herança multipla

'''
Quando uma classe filha herda de várias classes pai, ela é chamada de 
'''
class A:
    pass
class B:
    pass
class C(A,B):
    pass
