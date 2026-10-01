def somar(a,b):
    return a + b
     

def subtrair(a,b):
    return a - b

def multiplicar(a,b):
    return a * b

def dividir(a,b):
    return a / b

numero_1 = float(input("Digite um número: "))
numero_2 = float(input("Digite outro número: "))

resultado_smr = somar(numero_1,numero_2)
print(f"O resultado da soma é: {resultado_smr}")

resultado_sbt = subtrair(numero_1,numero_2)
print(f"O resultado da subtração é: {resultado_sbt}")

resultado_mlt = multiplicar(numero_1,numero_2)
print(f"O resultado da multiplicação é: {resultado_mlt}")

resultado_dvd = dividir(numero_1,numero_2)
print(f"O resultado da divisão é: {resultado_dvd}")