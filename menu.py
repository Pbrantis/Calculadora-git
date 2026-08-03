from calculadora import subtracao, dividir

OPERACOES = {
    "1": ("Subtração", subtracao),
}


def mostrar_menu():
    print("=== Calculadora Git ===")
    for codigo, (nome, _) in OPERACOES.items():
        print(f"{codigo} - {nome}")
    print("0 - Sair")


def executar():
    while True:
        mostrar_menu()
        escolha = input("Escolha uma operação: ").strip()
        if escolha == "0":
            print("Até a próxima!")
            break
        if escolha not in OPERACOES:
            print("Opção inválida. Tente novamente.")
            continue
        nome, funcao = OPERACOES[escolha]
        a = float(input("Primeiro número: "))
        b = float(input("Segundo número: "))
        try:
            resultado = funcao(a, b)
        except ValueError as erro:
            print(f"Erro: {erro}")
        else:
            print(f"{nome}: {resultado}")


def menu():
    while True:
        print("\n=== FEATURE: DIVISÃO ===")
        print("1. Dividir dois números")
        print("2. Sair")

        opcao = input("\nEscolha uma opção (1 ou 2): ")

        if opcao == "1":
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                resultado = dividir(num1, num2)
                print(f"\n Resultado: {num1} / {num2} = {resultado}")
            except ValueError as e:
                msg_erro = str(e) if str(e) else "Entrada inválida! Digite apenas números."
                print(f"\n Erro: {msg_erro}")
        elif opcao == "2":
            print("\nSaindo...")
            break
        else:
            print("\n Opção inválida! Escolha 1 ou 2.")


if __name__ == "__main__":
    menu()

if __name__ == "__main__":
    executar()

