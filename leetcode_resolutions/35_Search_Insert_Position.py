class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        if target < nums[0]:
            return 0

        if target > nums[-1]:
            return len(nums)

        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1

        return l
        
# Por que não usei mid = (l+r)//2 na linha 13?
# Por bom hábito, pois em linguagens que possuem limite por tipagem estática, que não é o caso de Python,
# mas de C ou C++ por exemplo, essa soma e divisao inteira por 2 pode acabar ultrapassando o limite de
# armazenamento do tipo da variável.
# Ao usar m = l + (r-l) // 2 impedimos esse erro, visto que desta forma utilizamos a distancia entre
# os 2 valores r e l, que com certeza dará um valor capaz de ser armazenado naquele tipo de variável.
# Em seguida, basta adicionar sua divisão inteira por 2 ao valor de l, resultando na nova posição de m. 