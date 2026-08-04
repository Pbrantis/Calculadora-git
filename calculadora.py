import math
def valor_absoluto(numero):
    if numero < 0:
        return -numero
    else:
        return numero

numero = float(input("Digite um número: "))

resultado = valor_absoluto(numero)

print("O valor absoluto é:", resultado)