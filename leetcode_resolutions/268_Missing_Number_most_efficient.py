class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = n * (n + 1) // 2
        return total - sum(nums)
    
# Este método usa apenas um fundamento básico da matématica,
# baseado no fato em que a soma de uma sequência de números
# subtraído de outra sequência de números de valor total menor
# resulta na soma dos valores faltantes na sequência de maior valor.
# Como neste problema existe apenas um número faltando, então este
# método sempre funciona, mesmo que na realidade retorne a soma dos
# valores faltantes.