# And = para ser true, ambos os lados devem ser true
# Or = para ser true, pelo menos um dos lados deve ser true
# Not = inverte o valor booleano


print(True and True)  # True
print(False and True)  # False
print(False and False)  # False
print(False or False)  # False
print(False or True)  # True
print(True or True)  # True



saldo = 1000 
saque = 250
limite = 200
conta_especial = True

exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(exp)  # True

exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)

print(exp_2)  # True