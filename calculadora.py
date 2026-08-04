import math

# numero = float(input("Digite um número: "))
# base = float(input("Digite a base do logaritmo: "))
#
# if numero > 0 and base > 0 and base != 1:
#     resultado = math.log(numero, base)
#     print("Resultado:", resultado)
# else:
#     print("Número ou base inválidos.")
def subtracao(a,b):
    return a-b

def soma(a,b):
    return a+b

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


# Testando a função
oposto = 10
adjacente = 5
resultado = calcular_tangente_triangulo(oposto, adjacente)
print(f"A tangente do ângulo é {resultado:.4f}")



def dividir(a, b):
    if b == 0:
        raise ValueError("Não é possível dividir por zero!")
    return a / b

