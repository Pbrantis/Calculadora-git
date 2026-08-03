def subtracao(a,b):
    return a-b


def derivada_parcial_numerica(f, ponto, var_index, h=1e-5):
    """
    Calcula o valor numérico da derivada parcial em um ponto.

    :param f: Função Python que aceita uma lista ou array de coordenadas.
    :param ponto: Lista/tupla com o ponto de avaliação, ex: [2.0, 3.0].
    :param var_index: Índice da variável em relação à qual derivar (0 para x, 1 para y, etc.).
    :param h: Passo de variação (valor pequeno).
    :return: Valor numérico da derivada no ponto.
    """
    ponto_mais = list(ponto)
    ponto_menos = list(ponto)

    ponto_mais[var_index] += h
    ponto_menos[var_index] -= h

    return (f(ponto_mais) - f(ponto_menos)) / (2 * h)


# --- Exemplo de uso ---
# Função Python: f(x, y) = x^3 * y + 2*x * y^2
def f(p):
    x, y = p[0], p[1]
    return x ** 3 * y + 2 * x * y ** 2


ponto = [2.0, 3.0]  # x = 2, y = 3

# ∂f/∂x no ponto (2, 3)
df_dx_val = derivada_parcial_numerica(f, ponto, var_index=0)

# ∂f/∂y no ponto (2, 3)
df_dy_val = derivada_parcial_numerica(f, ponto, var_index=1)

print(f"∂f/∂x em (2, 3) ≈ {df_dx_val:.4f}")  # Esperado: 3*(4)*(3) + 2*(9) = 54
print(f"∂f/∂y em (2, 3) ≈ {df_dy_val:.4f}")  # Esperado: 8 + 4*(2)*(3) = 32

