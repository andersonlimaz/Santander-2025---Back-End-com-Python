# Recursos Publicos e Privados
'''
Modificadores de Acesso

Em linguagens como java e C++, existem palavras reservadas para definir o nível de acesso aos atributos
e metodos da classe. Em pyhton não temos palavras reservadas, porém usamos converções no nome do recurso, 
para definir se a variavel é publica ou privada.

++Definição++

* Publico - pode ser acessado de fora da classe.
* Privado - Só pode ser acessado pela classe.

Publico/Privado

Todos os recursos são publicos em python, a menos que o nome inicie com underline "_".Ou seja, 
o interpretador Python não irá garantir a proteção do recurso, mas por uma conversão amplamente adotada na comunidade,
quando encontramos uma variavel e/ou metodo com nome iniciado por underline, sabemos que não deveriamos manipular
o seu valor diretamente, ou invocar o método fora do escopo da classe. 
'''
class Conta:
    def __init__(self,nro_agencia,saldo=0):
        self._saldo = saldo
        self.nro_agencia = nro_agencia

    def depositar(self,valor):
        self._saldo += valor
    
    def sacar(self, valor):
        self._saldo -= valor

    def mostrar_saldo(self):
        return self._saldo
    


conta = Conta("0001",100) 
conta.depositar(100)
print(conta.nro_agencia)
print(conta.mostrar_saldo)
