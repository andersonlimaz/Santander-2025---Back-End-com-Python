def validar_email(email):
    if " " in email:
        print("E-mail inválido")
    elif "@" not in email or email.startswith("@") or email.endswith("@"):
        print("E-mail inválido")
    else:
        partes = email.split("@")
        if len(partes) != 2:
            print("E-mail inválido")
        else:
            dominio = partes[1]
            if dominio == "gmail.com" or dominio == "outlook.com":
                print("E-mail válido")
            else:
                print("E-mail inválido")

# Entrada
email = input()
validar_email(email)
