from calculadora import dividir, media_aritmetica, subtracao, calcular_cosseno

OPERACOES = {
    "1": ("Subtração", subtracao),
    "2": ("Média Aritmética", media_aritmetica),
    "3": ("Cosseno", calcular_cosseno),
    "2": ("Divisão", dividir),
    "3": ("Média Aritmética", media_aritmetica),
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

        if escolha == "3":
            a = float(input("Digite o ângulo em graus: "))
            resultado = funcao(a)
        else:
            a = float(input("Primeiro número: "))
            b = float(input("Segundo número: "))
            resultado = funcao(a, b)

        try:
            # O bloco try/except permanece para tratar possíveis exceções
            pass
        except ValueError as erro:
            print(f"Erro: {erro}")
        else:
            print(f"{nome}: {resultado}")


if __name__ == "__main__":
    executar()
