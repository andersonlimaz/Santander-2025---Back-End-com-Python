def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)
exibir_poema("Sabado, 10 Outubro de 1967","Zen Of Python", "Beautiful is better than ugly.", autor="Tim Peters", ano=1999)
