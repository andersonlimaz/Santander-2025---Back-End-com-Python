'''
Parâmetros especiais

Por padrão, argumentos podem ser passados para uma função Python tanto por posição qunato explicitamente pelo nome. 
Para uma melhor legilidade e desempenho, faz sentido restringir a maneira pelo qual argumentos possam ser passados, 
assim um desenvolvedor precisa apenas olhar para a definição da função para determinar se os itens são passados por posição,
por posição e nome, ou por nome. 
'''
def criar_carro(modelo, ano, placa,/,marca,motor,combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)


criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.4 Turbo", combustivel="Gasolina")
# Em Python, quando você coloca uma barra / na lista de parâmetros de uma função, isso indica que todos os parâmetros anteriores à barra devem ser posicionais.
# criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.4 Turbo", combustivel="Gasolina")


