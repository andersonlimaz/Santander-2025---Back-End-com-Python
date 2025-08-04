# Objetivo desse projeto 
'''
Iniciar a modelagem do sistema bancario em POO. 
Adicionar classes para cliente e as operações bancarias: deposito e saque

Atualizar a implementação do sistema bancario, 
para armazenar os dados de clientes e contas bancarias em objetos ao inves de dicionarios. 
O Codigo deve seguir o modelo de classes UML a seguir:
'''
from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime
import textwrap

class Cliente:
    def __init__(self,endereco):
        self.endereco = endereco
        self.conta = []

    def transacao_conta(self,conta,transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.conta.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf,  endereco):
        super().__init__(endereco)
        self.nome=nome
        self.data_nasmento = data_nascimento
        self.cpf = cpf

class Conta:
    def __init__(self, numero, cliente ):
        self.saldo= 0
        self._numero = numero
        self.agencia = "0001"
        self.cliente = cliente
        self.historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
    
    @property
    def saldo(self):
        return self.saldo
    
    @property
    def agencia(self):
        return self.agencia
    
    @property
    def cliente (self):
        return self.cliente
    
    def sacar(self,valor):
        saldo =self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\n@@@ Operação falhou! Você não saldo suficiente. @@@")

        elif valor > 0:
            self._saldo -= valor
            print("\n ==== Saque realizado com sucesso ! ===")
            return True
        
        else:
            print("\n@@@ Operação falhou, O valor informado é invalido @@@")
        
        return False

    def depositar(self, valor):
        if valor > 0:
            self.valor += valor 
            print("\n=== deposito relizado com sucesso ===")
        else:
            print("\n @@@ Operação falhou! O valor informado é invalido. @@@")
            return False
        return True

class ContaCorrente(Conta): 
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero,cliente)
        self.limite=limite
        self.limite_saques= limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [transcao for transcao in self.historico.transacao if transcao if ["tipo"] == Saque.__name__]
    )
        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques

        if excedeu_limite:
            print("@@@ Operação falhou! O valor do saque excedeu o limite @@@")
        elif excedeu_saques:
            print("\n @@@ Operação falhou! Numeros maximo de saques exceditos! @@@")
        
        else:
            return super().sacar(valor)
        return False
    
    def __str__(self):
        return f"""\
            agência:\t{self.agencia}
            C\C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """

class Historico:

    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime
                ("%d-%m-%Y %H:%M:%s"),
                
            }
        )

class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass
    @abstractclassmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):

    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
         return self._valor 
    
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Deposito(Transacao):

    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
         return self._valor 
    
    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [ cliente for cliente in clientes if cliente.cpf == cpf] 
    return clientes_filtrados[0] if clientes_filtrados else None

def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("\n@@@ Cliente não possui conta ! @@@")
        return
    
    # FIXME: NÃO PERMITE CLIENTE ESCOLHER A CONTA
    return cliente.contas[0]

def depositar(clientes):
    cpf = input("informe o CPF do Cliente")
    cliente = filtrar_cliente(cpf,clientes)
    

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return
    valor = float(input("Informe o valor do depósito: "))
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    cliente.realizar_transacao(conta,transacao)

def menu():
   menu = """\n
   ============== MENU ==============
   [d]\tDepositar
   [s]\tSacar
   [e]\tExtrato
   [nc]\tNova Conta
   [lc]\tListar contas
   [nu]\tNovo usuário
   [q]\tSair
  ====> 
   """ 
   return input(textwrap.dedent(menu))
    
def sacar(clientas):
    cpf = input("Informe o CPF do cliente")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return
    valor = float(input("Informe o valor do saque: "))
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta,transacao)

def exibir_extrato(clientes):
    cpf =input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, cliente)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return
    
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    print("\n==================== EXTRATO ==============")
    transacoes = conta.historico.transacoes

    extrato = " "
    if not transacoes:
        extrato = "Não foram realizadas movimentações."
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}:\n\tR${transacao['valor']:.2f}"
    
    print(extrato)
    print(f"\nSaldo: \n\tR$ {conta.saldo:.2f}")
    print("============================")

def criar_conta(numero_conta, cliente, contas):
    cpf = input("informe o CPF ")
    cliente = filtrar_cliente(cpf,clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado, fluxo de criação de conta encerrado! @@@")
        return
    
    conta = ContaCorrente.nova_conta(cliente=cliente,numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)

    print("====== \n Conta criada com sucesso! =====")

def criar_cliente(clientes):
    cpf = input("informe o CPF (somente número):")
    cliente = filtrar_cliente(cpf,clientes)

    if cliente:
        print("\n@@@ Já existe cliente com esse CPF @@@")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nacimento(dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    cliente = PessoaFisica(nome=nome,data_nascimento=data_nascimento,cpf=cpf,endereco=endereco)
    
    clientes.append(cliente)

    print("\n ===== Cliente criado com sucesso! =====")

def listar_contas(contas):
    for conta in contas:
        print("=" * 100)
        print(textwrap.dedent(str(conta)))

def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao =="d":
            depositar(clientes)
        elif opcao == "s":
            sacar(clientes)
        elif opcao == "e":
            exibir_extrato(clientes)
        elif opcao == "nu":
            criar_cliente(clientes)
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)
        elif opcao == "lc":
            listar_contas(contas)
        elif opcao == "q":
            break
        else:
            print("\n@@@ Operação inválida, por favor selecione novamente a opração desejada. @@@")

main()