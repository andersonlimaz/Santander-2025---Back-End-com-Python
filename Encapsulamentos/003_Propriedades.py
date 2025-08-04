# Para que servem ?

'''
Com o property() do python, você pode criar atributos gerenciados em suas classes.
Você pode usar atributos gerenciados, também conhecidos como propiedades, quando 
presamos modificar sua implementação interna sem alterar a API publica da classe. 
'''
class Foo:
    def __init__(self, x=None):
        self._x = x

    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self,value):
        self._x += value

    @x.deleter
    def x(self):
        self._x =- 1

foo = Foo(10)
print(foo.x)
foo.x = 10
print(foo.x)
del foo.x
print(foo.x)