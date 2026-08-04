def subtracao(a,b):
    return a-b

def soma(a,b):
    return a+b

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
  
def maximo(a, b):
    return max(a, b)

def dividir(a, b):
    if b == 0:
        raise ValueError("Não é possível dividir por zero!")
    return a / b

def calcular_exponencial(x):
    resultado = 0
    # 20 repetições (termos) garantem uma excelente precisão
    for n in range(20):
        termo = (x ** n) / calcular_fatorial(n)
        resultado += termo
    return resultado
def calcular_cosseno(angulo_graus):
    import math

    return math.cos(math.radians(angulo_graus))

import math

def logaritmo(numero, base):
    if numero > 0 and base > 0 and base != 1:
        return math.log(numero, base)
    return "Número ou base inválidos."

# TESTANDo
