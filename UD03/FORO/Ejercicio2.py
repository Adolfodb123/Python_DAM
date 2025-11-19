def imprimir_estrella_ocho_puntas(n):
    if n % 2 == 0 or n < 3:
        print("El tamaño debe ser un número impar mayor o igual a 3.")
        return

    matriz = [[" " for _ in range(n)] for _ in range(n)]
    centro = n // 2

    for i in range(n):

        matriz[i][centro] = "*"

        matriz[centro][i] = "*"

        matriz[i][i] = "*"

        matriz[i][n - 1 - i] = "*"

    for fila in matriz:
        print("".join(fila))

imprimir_estrella_ocho_puntas(9)
