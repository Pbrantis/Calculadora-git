def calcular_porcentagem():
    try:
        valor = float(input("Digite o valor base: "))
        porcentagem = float(input("Digite a porcentagem que deseja calcular: "))

        resultado = (valor * porcentagem) / 100
        print(f"➔ {porcentagem}% de {valor} é: {resultado}\n")
    except ValueError:
        print("Erro: Por favor, digite apenas números.\n")

