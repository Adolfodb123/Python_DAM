def letra_M(n):
    if n < 3 or n % 2 == 0:
        print("El tamaño debe ser un número impar mayor o igual a 3.")
        return

    for i in range(n):
        fila = ""
        for j in range(n):
            if j == 0 or j == n - 1:  
                fila += "*"
            elif i == j and i <= n // 2:  
                fila += "*"
            elif j == n - 1 - i and i <= n // 2:  
                fila += "*"
            else:
                fila += " "
        print(fila)

letra_M(7)
