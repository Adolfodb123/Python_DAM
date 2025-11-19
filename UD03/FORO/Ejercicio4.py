def cuadrado_con_diagonales(n):
    if n < 3:
        print("El tamaño debe ser mayor o igual a 3.")
        return

    for i in range(n):
        fila = ""
        for j in range(n):
            if (
                i == 0 or i == n - 1
                or j == 0 or j == n - 1 
                or i == j 
                or j == n - 1 - i  
            ):
                fila += "*"
            else:
                fila += " "
        print(fila)

cuadrado_con_diagonales(7)
