#arquivo = open("text.txt", "r", encoding="utf-8")
#conteudo = arquivo.read()
#print(conteudo)
#arquivo.close()

#### LENDO O CONTEUDO
with open("text.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
#### ESCREVENDO UM NOVO CONTEUDO (Modo A)
with open("text.txt", "a", encoding="utf-8") as arquivo:
    texto = "\n e mais uma ves o destino nos afronta"
    arquivo.write(texto)