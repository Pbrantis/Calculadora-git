import calculadora


def exibir_menu():
    while True:
        print("=== MENU DE OPÇÕES ===")
        print("1. Calcular Porcentagem")
        print("2. Calcular Resto da Divisão")
        print("3. Sair")

        opcao = input("Escolha uma opção (1-3): ")
        print("-" * 22)

        if opcao == "1":
            calculadora.calcular_porcentagem()
        elif opcao == "2":
            calculadora.resto_divisao()
        elif opcao == "3":
            print("Saindo do programa... Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.\n")


# Executa o menu quando o arquivo é iniciado
if __name__ == "__main__":
    exibir_menu()
