def criar_carro(modelo, ano, placa,/,*,marca,motor,combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.4 Turbo", combustivel="Gasolina")
criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.4 Turbo", combustivel="Gasolina")