
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
