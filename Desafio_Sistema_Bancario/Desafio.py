import textwrap
def menu():
    menu = """\n

    ================== MENU ===============
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tListar Usuario
    [5]\tNovo Usuario
    [6]\tSair
    =>"""
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("\n=== Deposito realizado com sucesso!===")
    else:
        print('\n ***Operação falhou! O valor informado é invalido***')

    return saldo,extrato

def sacar(*,saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite     
    excedeu_saques = valor > limite_saques

    if excedeu_saldo:
        print("***Operação falhou! Você não tem saldo suficiente***")

    elif excedeu_limite:
        print("***Operaçõa falhou! Ovalor do saque excede o limite.*** ")

    elif excedeu_saques:
        print("***Operação falhou! Número máximo de saque excedidos***")
         
    elif valor > 0:
        saldo -= valor
        extrato += f"===Saque: R$ {valor:.2f}\t==="
        numero_saques += 1
        print("\t === Saque realizado com sucesso!")

    else: 
        print("***Operação falhou! O valor informado não é inválido.***")
    
    return saldo,extrato

def exibir_extrato(saldo,/,*,extrato):
    print("\n ***************** EXTRATO ******************")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R${saldo:.2f}")
    print("*************************************************")

def criar_usuario(usuarios):
    cpf = input("informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf,usuarios)
    
    if usuario:
        print("\n*** Já existe usuario com esse CPF!***")
        return
    nome = input("informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa)")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    usuario.append({"nome":nome, "data_nascimento": data_nascimento, "cpf": cpf, "enderco": endereco})

    print("=== Usuario criado com sucesso ! ===")

def filtrar_usuario(cpf,usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] ==cpf ]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuario):
    cpf = input("informe o cpf do usuario: ")
    usuario = filtrar_usuario(cpf,usuario)

    if usuario:
        print("\n===Conta criada com sucesso!===")
        return{"agencia":agencia,"numero_conta":numero_conta,"usuario":usuario}
    print("\n*** Usuario não encontrado, fluxo de criação de conta encerrado!***")

def lista_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agência']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
    """
    print("=" * 100)
    print(textwrap.dedent(linha))


def main():
    LIMITE_SAQUES = 3
    AGENCIA ="0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:

        opcao = menu()
        
        if opcao =="1":
            valor = float(input("Informe o valor do depósito: R$"))
            saldo, extrato = depositar(saldo,valor,extrato)
        
        elif opcao =="2":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                limite_saques=LIMITE_SAQUES,
                numero_saques=numero_saques
            )

        elif opcao =="3":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "4":
            criar_usuario(usuarios)

        elif opcao =="5":
            numero_conta =len(contas) + 1
            conta = criar_conta(AGENCIA,numero_conta,usuarios)

            if conta:
                contas.append(conta)
        
        elif opcao =="lc":
            lista_contas(contas)

        elif opcao == "6":
            break

        else:
            print("Operação inválida, por favor selecione a operação desejada.")


main()
