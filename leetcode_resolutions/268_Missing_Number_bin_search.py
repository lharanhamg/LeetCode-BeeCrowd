class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        l, r = 0, len(nums)-1
        while l <= r:
            m = l + (r - l)//2
            if nums[m] == m:
                l = m + 1
            elif nums[m] > m:
                r = m - 1
        return l
    
# Explicação: se o nums[m] coincide com o índice m, então todos os elementos
# estão presentes até aquele elemento, desde o 0 até ele de forma crescente.
# O único caso diferente seria em que o nums[m] > m, visto que se eu retiro
# um elemento, os índices serão obrigatoriamente menores que os valores
# daquela posição.
#
# Exemplo: [0,1,2,3,4,6]
# Aqui falta o 5, mas até o número 4 os índices estão alinhados com seus
# respectivos valores. A partir do índice m=5, observa-se que os índices
# subsequentes não coincidem com o valor respectivo, sendo estes valores
# sempre maiores do que seus índices, justamente pela exclusão do número 5.