# Solicitando os dados do paciente
nome = input("Informe o nome: ")
idade = int(input("Informe a idade: "))

if idade == 0:
    situacao = "RN"
elif idade <= 3:
    situacao = "Bebê"
elif idade <= 10:
    situacao = "Criança"
elif idade <= 14:
    situacao = "Adolescente"
elif idade <= 30:
    situacao = "Jovem"
elif idade <= 64:
    situacao = "Adulto"
else:
    situacao = "Vintage"

print:(f"O paciente {nome} tem {idade} sua classificação é {situacao}")