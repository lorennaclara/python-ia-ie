# Criando dicionário composto de cadastro de funcionário
funcionarios = {
    "44356":{
            "nome":"Vitor Davi", 
             "telefone": "11912121315",
             "data_nascimento":"10/12/2010",
             "cargo":"Jovem Aprendiz",
             "habilidades":["front-end","java","python"]
    },
    "42568": {
            "nome":"Michael Jackson", 
             "telefone": "11204859090",
             "data_nascimento":"29/08/1958",
             "cargo":"Rei do pop",
             "habilidades":["dançarino","cantor","compositor"]

    },
    "43900":{
            "nome":"George Michael", 
             "telefone": "11567585999",
             "data_nascimento":"25/06/1963",
             "cargo":"Cantor",
             "habilidades":["produtor","cantor","compositor"]

    }

}

print(funcionarios["42568"]["habilidades"][1])