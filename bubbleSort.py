lista = [4,2,1,6,10,12,5,7]

def bubbleSort(lista: list):
    rango = len(lista) - 1
    for j in range(rango):
        for i in range(rango - j):
            if lista[i] > lista[i + 1]:
                temp = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = temp
        print(f" {j + 1} : {lista}")
       

bubbleSort(lista)

lista_desordenada = [
    37, 4, 29, 15, 48, 9, 23, 41, 2, 50,
    18, 33, 7, 45, 12, 27, 39, 1, 30, 19,
    44, 6, 25, -14, 49, 11, 36, 3, 31, 22,
    47, 5, 28, 16, 40, 8, 24, 43, 10, 34,
    21, 38, 13, 46, 17, 26, 42, 20, 35, 32
]

bubbleSort(lista_desordenada)
