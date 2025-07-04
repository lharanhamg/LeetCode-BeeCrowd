"""
    Escrever o código para função de soma recursiva.

    args: lista(array) de inteiros

    return: int
    
"""

def soma_recursiva(lista):
    if not lista:
        return 0
    
    return lista.pop(0) + soma_recursiva(lista)

print(soma_recursiva([1,2,3,4,5]))