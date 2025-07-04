class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        # Minha solução utiliza binary search, que só funciona
        # em iteráveis já ordenados de forma crescente.
        # Complexidade Temporal: O(log n)
        nums1.sort()
        nums2.sort()

        # Pensei em fazer o ans ser uma array e só ao fim fazer list(set(ans)),
        # mas não seria tão eficiente quanto iniciar o ans como set de imediato.
        ans = set()

        # for externo: controla o índice de nums1
        for i in range(len(nums1)):

            # Reiniciar as variáveis l e r sempre que for
            # buscar por outro número de nums1 em nums2!
            l, r = 0, len(nums2) - 1

            # while interno: efetua binary search em nums2
            # em busca do valor nums1[i]
            while l <= r:
                # Reinicio o ponteiro m em cada iteração
                # da busca por binary search, tentando
                # sempre reduzir pela metade o espaço amostral.
                m = l + (r - l) // 2

                if nums2[m] == nums1[i]:
                    # Como iniciei ans como set, usa-se o método add()
                    ans.add(nums1[i])
                    # Como já encontrei o valor buscado, posso interromper
                    # o loop interno que busca em nums2
                    break

                # Lógica base de Binary Search
                elif nums2[m] < nums1[i]:
                    l = m + 1
                else:
                    r = m - 1
                    
        # Conversão implícita do ans de set para list,
        # visto que o retorno deve ser uma lista.
        return list(ans)