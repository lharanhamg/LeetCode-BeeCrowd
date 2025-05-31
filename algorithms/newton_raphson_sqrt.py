# Implementações genéricas do algoritmo de Newton-Raphson para encontrar a raíz de um número.
# Para melhor compreensão, explicação detalhada em leetcode_resolutions/367_Valid_Perfect_Square.py

# Versão apenas para inteiros:

def sqrt_integer_newton(n: int) -> int:
    """
    Retorna a raíz quadrada inteira de um número inteiro positivo usando o método de Newton-Raphson.
    Se não for quadrado perfeito, retorna o piso da raíz.
    """
    if n < 2:
        return n  # 0 ou 1 são casos triviais

    x = n // 2  # chute inicial
    while x * x > n:
        x = (x + n // x) // 2  # fórmula inteira
    return x if x * x == n else -1  # retorna -1 se não for quadrado perfeito

# Versão que admite valores de ponto flutuante:

def sqrt_float_newton(n: float, epsilon: float = 1e-10, max_iter: int = 1000) -> float:
    """
    Retorna a raíz quadrada de um número positivo (float) usando o método de Newton-Raphson.
    Utiliza critério de tolerância para convergência e limite de iterações.
    
    Parâmetros:
    - n: número real positivo
    - epsilon: tolerância máxima de erro absoluto
    - max_iter: número máximo de iterações

    Retorna:
    - Aproximação da raíz quadrada de n como float
    """
    if n < 0:
        raise ValueError("Não é possível calcular a raíz quadrada de número negativo.")
    if n == 0:
        return 0.0

    x = n / 2  # chute inicial
    for _ in range(max_iter):
        x_next = (x + n / x) / 2
        if abs(x - x_next) < epsilon:
            return x_next
        x = x_next

    return x  # retorna após atingir max_iter se não convergir
