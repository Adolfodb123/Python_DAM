def cuadrado_con_diagonales_y_cuadro(n):
    if n < 5 or n % 2 == 0:
        print("El tamaño debe ser un número impar mayor o igual a 5.")
        return

    centro = n // 2
    for i in range(n):
        fila = ""
        for j in range(n):
            if (
                i == 0 or i == n - 1 or
                j == 0 or j == n - 1 or
                i == j or 
                j == n - 1 - i 
            ):
                fila += "*"
            elif (
                centro - 1 <= i <= centro + 1 and
                centro - 1 <= j <= centro + 1
            ):
                # cuadro interno hueco (se deja vacío)
                fila += " "
            else:
                fila += " "
        print(fila)


# Ejemplo de uso
cuadrado_con_diagonales_y_cuadro(9)
