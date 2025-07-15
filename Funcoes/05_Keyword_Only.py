'''parâmetros que vêm depois dele devem ser passados obrigatoriamente como argumentos nomeados, ou seja, com o nome do parâmetro explícito na chamada.
Símbolo	Significado	Efeito
/	Parâmetros anteriores devem ser posicionais	Não podem ser nomeados na chamada
*	Parâmetros seguintes devem ser nomeados	Chamada deve incluir nome=valor'''
def criar_carro(*,modelo, ano, placa,marca,motor,combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.4 Turbo", combustivel="Gasolina")
# criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.4 Turbo", combustivel="Gasolina")