"""
    Encontra o maior valor em uma lista, usando recursividade.

    args: lista (array) de inteiros.

    return: int.

"""

def maior(lista, y = float('-inf')):
    if not lista:
        return y
    
    x = lista.pop(0)

    if x > y:
        y = x

    return maior(lista, y)

print(maior([1,2,3,4,5]))
