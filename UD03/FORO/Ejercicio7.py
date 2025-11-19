def triangulo_invertido(n):
    if n < 2:
        print("La altura debe ser mayor o igual a 2.")
        return

    for i in range(n):
        if i == 0 or i == n - 1:
            print("*" * n)
        else:
            fila = "*"
            if i % 2 == 0:
                fila += " " * (n - 2)
            else:
                for j in range(n - 2):
                    if j % 2 == 0:
                        fila += "*"
                    else:
                        fila += " "
            fila += "*"
            print(fila)

triangulo_invertido(6)
