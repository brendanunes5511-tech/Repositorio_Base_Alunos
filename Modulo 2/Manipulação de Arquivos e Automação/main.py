import csv

print("=== sistema de notas ===")

    opcao = input("[1]- Cadastrar aluno e nota\n" \
    "[2] - listar alunos\n" \
    "[3] - listar alunos com nota acima de 8\n" \
    "[0] - sair\nSua opção: ")

    if opcao == "1":
        nome = input ("nome: ")
        idade = input ("idade: ")
        nota = input ("nota: ")
        with open ("alunos.csv","a", newfile="") as arquivo:
           csv.writer(arquivo).writerow([nome,idade,nota])
        print("aluno cadastrado")
    elif opcao =="2":
        arquivo = open("alunos.csv", "r")

        for linha in arquivo:
            print(linha)
        arquivo.close()
        
    elif opcao =="3":
        print("listar alunos com notas acima de 8")
    elif opcao =="0":
        print("saindo...")
        break
    else:
        print("opção invalida.")