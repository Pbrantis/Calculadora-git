import math

numero = float(input("Digite um número: "))
base = float(input("Digite a base do logaritmo: "))

if numero > 0 and base > 0 and base != 1:
    resultado = math.log(numero, base)
    print("Resultado:", resultado)
else:
    print("Número ou base inválidos.")
def subtracao(a,b):
    return a-b

def soma(a,b):
    return a+b

def dividir(a, b):
    if b == 0:
        raise ValueError("Não é possível dividir por zero!")
    return a / b

