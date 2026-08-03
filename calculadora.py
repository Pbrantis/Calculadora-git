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

def media_aritmetica(a, b):
    return (a + b) / 2

def dividir(a, b):
    if b == 0:
        raise ValueError("Não é possível dividir por zero!")
    return a / b

def calcular_fatorial(n):
    if n == 0 or n == 1:
        return 1
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

def calcular_tangente_triangulo(cateto_oposto, cateto_adjacente):
    if cateto_adjacente == 0:
        return "Erro: O cateto adjacente não pode ser zero."

    tangente = cateto_oposto / cateto_adjacente
    return tangente

