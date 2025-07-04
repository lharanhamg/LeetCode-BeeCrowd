from collections import deque
def condition(item):
    #
    # Código de condição
    #
    return item

def bfs(hmap, pivot_item):
    # Crio a fila com o deque().
    fila = deque()
    # Adiciono o valor no dicionário de um item pivô.
    fila += hmap[pivot_item]
    # Crio o conjunto dos visitados para evitar loop.
    visitados = set()

    while fila:
        # Remove o primeiro elemento da fila para analisar.
        objt_analisado = fila.popleft()

        # Checa se já visitamos aquele vértice do grafo.
        if objt_analisado not in visitados:
            # Analisa se a condição buscada é verdadeira.
            if condition(objt_analisado):
                # Retorna verdadeiro se achar o caminho no grafo.
                return True
            else:
                # Adiciona os vizinhos do objeto analisado na fila;
                # Método get() retorna o valor da chave passada e retorna []
                # se a chave não existir no dicionário.
                fila += hmap.get(objt_analisado, [])
                # Adiciona o objeto analisado aos visitados para não causar loop.
                visitados.add(objt_analisado)

    # Retorna falso se não existir caminho pelo grafo para o que procuramos.
    return False