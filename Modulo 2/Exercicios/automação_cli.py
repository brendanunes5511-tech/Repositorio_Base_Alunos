import os

#os.getcwd() - Mostra a pasta atual
#os.lisdir() - Lista arquyivos e pastas
#os.mkdir("pasta") - cria uma pasta
#os.remove("pasta") - remove uma pasta
#shutil.move("origem", "destino") - move uma pasta de origem ao destino
#os.system("comando") - executar um comando.
print("criador de pasta")
pasta = input("digite o nome da pasta que deseja criar: ")
os.mkdir(pasta)