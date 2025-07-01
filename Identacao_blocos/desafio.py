'''Desafio
Fomos contratados por um grande banco para desenvolver o seu novo sistema Esse banco deseja modernizar suas operações e para isso 
escolheu a linguagem Python. Para a primeira versão do sistema devemos implementar apenas 3 operações: depósito, saque e extrato.

'''


menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sai

=>"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)
    
    if opcao =="1":
        valor = float(input("Informe o valor do depósito: R$"))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print('Operação falhou! O valor informado é invalido')
    
    elif opcao =="2":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite
       
        excedeu_saques = valor > LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente")

        elif excedeu_limite:
            print("Operaçõa falhou! Ovalor do saque excede o limite. ")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saque excedidos")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"

        else: 
            print("Operação falhou! O valor informado não é inválido.")


    elif opcao =="3":
        print("\n ***************** EXTRATO ******************")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R${saldo:.2f}")
        print("*************************************************")
    
    elif opcao == "4":
        break

    else:
        print("Operação inválida, por favor selecione a operação desejada.")