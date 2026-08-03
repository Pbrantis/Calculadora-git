def calcular_porcentagem():
    try:
        valor = float(input("Digite o valor base: "))
        porcentagem = float(input("Digite a porcentagem que deseja calcular: "))

        resultado = (valor * porcentagem) / 100
        print(f"➔ {porcentagem}% de {valor} é: {resultado}\n")
    except ValueError:
        print("Erro: Por favor, digite apenas números.\n")


def resto_divisao():
    try:
        dividendo = int(input("Digite o dividendo (número que será dividido): "))
        divisor = int(input("Digite o divisor (número que vai dividir): "))

        if divisor == 0:
            print("Erro: Não é possível dividir por zero.\n")
            return

        resultado = dividendo % divisor
        print(f"➔ O resto da divisão de {dividendo} por {divisor} é: {resultado}\n")
    except ValueError:
        print("Erro: Por favor, digite apenas números inteiros.\n")
