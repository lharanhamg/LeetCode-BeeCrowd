"""
    Escrevendo a função quicksort.

    args: lista (array) de inteiros possivelmente desordenados.

    return: lista (array) de inteiros ordenados.

"""

def qsort(lista):
    if len(lista) < 2:
        return lista
    
    middle = len(lista) // 2
    pivot = lista[middle]

    lower = []
    mid = []
    higher = []

    for i in range(len(lista)):
        if lista[i] < pivot:
            lower.append(lista[i])
        elif lista[i] == pivot:
            mid.append(lista[i])
        else:
            higher.append(lista[i])

    return qsort(lower) + mid + qsort(higher)

print(qsort([3, 5, 2, 1, 4]))