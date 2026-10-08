nome = input("Digite seu nome: ")
email = input("Digite seu e-mail: ")

arquivo = open("7-pessoas.txt","a",encoding="utf-8")
arquivo.write(f"{nome} | {email} \n")
arquivo.close()

with open("7-pessoas.txt","a",encoding="utf-8") as arquivo: 
    arquivo.write(f"{nome} | {email} \n")