# Solicitando idade e altura
idade = int(input("Digite sua idade:"))
altura = float(input("Digite sua altura: ")) 

# Verificando a idade e altura
acesso = (idade >= 12) and altura >= 1.40

# Apresentando o resultado
print("Entrada Permitida: ", acesso)