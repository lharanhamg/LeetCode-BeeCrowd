# Solução por Binary Search:
# Complexidade Temporal: O(log n) | Complexidade Espacial: O(1)

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 0, num
        while l <= r:
            m = l + (r - l) // 2
            if m*m == num:
                return True
            elif m*m < num:
                l = m + 1
            else:
                r = m - 1
        return False
    
# Solução por Algoritmo de Newton-Raphson:

# Converge de forma quadrática para a raíz do número especificado.
# Isso significa que a cada tentativa, a quantidade 
# de casas decimais dobra, chegando cada vez mais próximo
# Exemplo: Se o erro atual é 0.01, o próximo erro será na ordem de 0.0001!
# Geralmente leva entre 3 a 6 tentativas, diferentemente do Binary Search,
# que precisa sempre de O(log n) tentativas para chegar ao resultado.

# A fraqueza deste algoritmo é quando usamos um chute inicial muito pequeno,
# causando o próximo chuta a tender pro infinito, ou então em funções
# com comportamento anômalo(uma função descontínua por exemplo).

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # Se o número for menor que 2 e positivo, 
        # sua raíz existe e será ele mesmo. 
        if num < 2:
            return True

        # A estratégia começa com um chute inicial de um valor
        # para ser a raíz do número 
        x = num // 2

        # Caso o quadrado do chute inicial seja maior que o número buscado,
        # utiliza a fórmula de Newton-Raphson para gerar um novo valor de chute.
        # Consiste basicamente de uma média entre x e num//x, que acaba convergindo
        # rapidamente em direção à raíz de num.
        while x * x > num:
            x = (x + num // x) // 2  # versão para inteiros da fórmula Newton-Raphson

        # Assim que sair do loop, ou seja, x*x <= num, o algoritmo retorna um booleano
        # sendo True se o quadrado do chute for igual ao número buscado,
        # e False caso contrário, indicando que sua raíz inteira não existe.
        return x * x == num
    
    # Exemplificação:
        # Queremos saber se 36 é um quadrado perfeito
        # √36 = 6 → queremos encontrar esse valor usando Newton-Raphson

        # num = 36

        # Começamos com um chute inicial: metade do número
        # x = num // 2  # x = 18

        # Aplicamos a fórmula de Newton-Raphson:
        # x_next = (x + num // x) // 2

        # Iterações:
        # 1ª: x = (18 + 36 // 18) // 2 = (18 + 2) // 2 = 10
        # 2ª: x = (10 + 36 // 10) // 2 = (10 + 3) // 2 = 6
        # 3ª: x = (6 + 36 // 6) // 2 = (6 + 6) // 2 = 6

        # Agora, x * x = 6 * 6 = 36 → é um quadrado perfeito 