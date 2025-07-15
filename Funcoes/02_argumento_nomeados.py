def salvar_carro(marca, modelo, ano, placa):
    #salva carro no banco de dados...
    print(f"carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

salvar_carro("fiat","palio", 1999, "ABC-1234")
salvar_carro(marca="fiat",modelo="palio",ano=1999, placa="ABL-1234")
salvar_carro(**{"marca":"fiat", "modelo":"Palio","ano":1999,"placa":"ABC-1234"})
