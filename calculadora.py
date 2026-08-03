import math
def subtracao(a,b):
    return a-b

def soma(a,b):
    return a+b

def raiz_quadrada(numero):
    if numero < 0:
        return "Não existe raiz quadrada real de número negativo."
    else:
        return math.sqrt(numero)


# Entrada de dados
numero = float(input("Digite um número: "))

# Chamada da função
resultado = raiz_quadrada(numero)

# Saída
print("A raiz quadrada é:", resultado)