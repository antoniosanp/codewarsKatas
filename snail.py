def snail(lista: list):
    n = len(lista)
    estado = "a"
    item = 0
    ordenado = []

    inicio = 0
    final = n - 1

    while item < n*n:

        if estado == "a":
            for col in range(inicio, final+1):
                ordenado.append(lista[inicio][col])
                item += 1
            estado = "b"


        elif estado == "b":
            for fila in range(inicio+1, final+1):
                ordenado.append(lista[fila][final])
                item += 1
            estado = "c"


        elif estado == "c":
            for col in range(final-1, inicio-1, -1):
                ordenado.append(lista[final][col])
                item += 1
            estado = "d"

        elif estado == "d":
            for fila in range(final-1, inicio, -1):
                ordenado.append(lista[fila][inicio])
                item += 1

            inicio += 1
            final -= 1
            estado = "a"

    return ordenado



    
matriz_10x10 = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
    [31, 32, 33, 34, 35, 36, 37, 38, 39, 40],
    [41, 42, 43, 44, 45, 46, 47, 48, 49, 50],
    [51, 52, 53, 54, 55, 56, 57, 58, 59, 60],
    [61, 62, 63, 64, 65, 66, 67, 68, 69, 70],
    [71, 72, 73, 74, 75, 76, 77, 78, 79, 80],
    [81, 82, 83, 84, 85, 86, 87, 88, 89, 90],
    [91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
]

lista = snail(matriz_10x10)

print(lista)
