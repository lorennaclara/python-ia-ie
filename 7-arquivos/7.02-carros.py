import csv

dados_tabela = [
    ["BAIRRO","CIDADE","ESTADO","CEP"],
    ["Jardim Paulista","Itapevi","SP","06663123"],
    ["Jardim Belval","Barueri","SP","06596991"],
    ["Suburbano","Itapevi","SP","06759087"],
    ["Centro","Jandira","SP","06759030"]
]

with open("7.02-cidades.csv","w",encoding="utf=8",newline="") as arquivo_csv:
    escrevendo = csv.writer(arquivo_csv)
    escrevendo.writerows(dados_tabela)