conta_normal = False
conta_universitaria = False
saldo = 2000
saque = 1500
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")

    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com cheque especial!")

    else:
        print("Não foi possivel realizar saque")

elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente para saque!")
else:
    print("Conta não identificada, não foi possivel realizar saque!")