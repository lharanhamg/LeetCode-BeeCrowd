# Pythonic Way: 
# Complexidade Temporal: O(n+m) | Complexidade Espacial: O(n+m)
from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d1 = dict(Counter(nums1))
        d2 = dict(Counter(nums2))
        ans = []

        for key in d1:
            if key in d2:
                if d1[key] <= d2[key]:
                    min_count = d1[key]
                else:
                    min_count = d2[key]
                for _ in range(min_count):
                    ans.append(key)
        return ans

# Opção 2:  
# Complexidade Temporal: O(n log n + m log m) | Complexidade Espacial: O(1)
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        

        # O método .sort() é built-in em Python, e é um algoritmo altamente otimizado
        # chamado de Timesort, um algoritmo híbrido entre merge sort e insertion sort,
        # Melhor caso(já parcialmente ordenado): O(n) | Caso Médio e Pior Caso: O(n * log n)
        # A diferença entre .sort() e .sorted() é que o primeiro muda o array original,
        # enquanto o segundo cria uma nova lista como resposta, sem alterar a anterior.
        nums1.sort()
        nums2.sort()
        i = 0
        j = 0
        ans = []
        # Two Pointers
        while i<len(nums1) and j<len(nums2):
            # Como já fizemos o sort dos arrays anteriormente,
            # podemos ter certeza de que se os valores nums[i] e nums[j]
            # diferem, então significa que já não há mais repetições
            # de nums[i] em nums[j].
            # Portanto, podemos apenas comparar de forma linear os valores dos arrays
            # tendo a garantia de que estamos adicionando apenas a interseção
            # entre os arrays e repetindo a quantidade de vezes em comum entre eles.
            if nums1[i] < nums2[j]:
                i+=1
                
            elif nums1[i] > nums2[j]:
                j+=1
                
            else:
                ans.append(nums1[i])
                i+=1
                j+=1
        return ans