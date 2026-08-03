def subtracao(a,b):
    return a-b

def soma(a,b):
    return a+b# operacoes.py

def dividir(a, b):
    if b == 0:
        raise ValueError("Não é possível dividir por zero!")
    return a / b