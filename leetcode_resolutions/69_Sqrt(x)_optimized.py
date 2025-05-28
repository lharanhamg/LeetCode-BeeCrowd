class Solution:
    def mySqrt(self, x: int) -> int:

        # Se o número for menor que 2, sua raíz será ela mesma, 
        # visto que o problema não admite valores negativos para x.
        if x < 2:
            return x
        for i in range(1, (x//2) + 1):
            # Checa se i é maior ou igual que a raiz de x e se o seu sucessor é maior que x na mesma iteração,
            # pois precisamos do inteiro mais próximo da raíz de x.
            if i*i <= x and (i+1)*(i+1) > x:
                return i