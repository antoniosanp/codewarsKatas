def snail(lista: list):
    n = len(lista) 
    estado = "a"
    item = 0
    ordenado = []
    print(n*n)
    inicio = 0
    final  = n - 1
  

    while item < 90 :
        if estado == "a":
            print("cambio")
            for i in range(inicio,final + 1):
                if i != final :
                    elemento = lista[inicio][i]
                    print(elemento)
                    ordenado.append(elemento)
                    item += 1
                if i == final :
                    estado = "b"
                    break

        if estado == "b":
            print("Cambio")
            for i in range(inicio,final + 1):
                if i != final :
                    elemento = lista[inicio + i][final]
                    print(elemento)
                    ordenado.append(elemento)
                    item += 1
                if i == final :
                    estado = "c"
                    break
        if estado == "c":
            print("Cambio")

            for i in range(inicio,final + 1):
                if i != final:
                    elemento = lista[final][final - i]
                    print(elemento)
                    ordenado.append(elemento)
                    item += 1
                if i == final:
                    estado = "d"
                    break
        if estado == "d":
            print("Cambio")
            for i in range(inicio,final + 1):
                if i != final :
                    elemento = lista[final - i][inicio]
                    print(elemento)
                    ordenado.append(elemento)
                    item += 1
                if i == final :
                    inicio += 1
                    final -= 1
                    estado = "a"
                    break
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
