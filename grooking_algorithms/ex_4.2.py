"""
    Conta o número de itens em uma lista.

    args: lista (array) de inteiros.

    return: int.

"""

def contador(lista):
    if not lista:
        return 0
    lista.pop(0)
    
    return 1 + contador(lista)

print(contador([1,2,3,4,5]))