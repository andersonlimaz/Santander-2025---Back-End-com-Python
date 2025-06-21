opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n"))

    if opcao == 1:
        print("Saque realizado com sucesso!")
    elif opcao == 2:
        print("Exibindo extrato...")
else:
    print("Obrigado por utilizar nosso sistema!")