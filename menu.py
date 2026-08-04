
from calculadora import subtracao, dividir, media_aritmetica, maximo


OPERACOES = {
    "1": ("Subtração", subtracao),
    "2": ("Divisão", dividir),
    "3": ("Média Aritmética", media_aritmetica),
    "4": ("Máximo entre dois números", maximo)

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

if __name__ == "__main__":
    executar()

