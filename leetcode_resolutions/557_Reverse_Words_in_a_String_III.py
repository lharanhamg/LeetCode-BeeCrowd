class Solution:
    def reverseWords(self, s: str) -> str:
        ans = ''
        l, r = 0, 0
                
        while r < len(s):

            # Se s[r] não for espaço...
            if s[r] != ' ':
                # Caso seja a última palavra, não entraria no else, pois não haveria espaço ao fim dela.
                # Dessa forma, adicionei manualmente essa verificação e concatenação.
                if r == len(s) - 1:
                    ans += s[l:r+1][::-1]
                # Adiciona uma posição à r.
                r += 1

            # Se s[r] for espaço...
            else:
                # Vai adicionar os caracteres, de trás para frente, até o espaço, sem incluí-lo.
                # Neste momento o r está na posição anterior ao espaço.
                ans += s[l:r][::-1]
                # Adiciona o espaço que faltou na concatenação.
                ans += ' '
                # Adiciona mais um em r, para que na próxima iteração ele comece na posição do espaço.
                r += 1
                # Iguala l com r, para recomeçar o processo na próxima palavra.
                l = r

        return ans