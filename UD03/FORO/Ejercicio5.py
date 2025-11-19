def cruz_borde_punteado(n):
    if n < 3 or n % 2 == 0:
        print("El tamaño debe ser un número impar mayor o igual a 3.")
        return

    centro = n // 2

    for i in range(n):
        fila = ""
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                fila += "."
            elif i == centro or j == centro:
                fila += "*"
            else:
                fila += " "
        print(" ".join(fila))

cruz_borde_punteado(7)
