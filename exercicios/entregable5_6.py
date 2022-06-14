def pares_impares(lista):

    pares = [n for n in lista if n % 2 == 0]
    impares = [n for n in lista if n % 2 != 0]
    pares.sort()
    impares.sort()
    return pares, impares

lista = [6, 5, 2, 1, 7]
pares, impares = pares_impares(lista)
print('Pares: ', pares)
print('Impares: ', impares)