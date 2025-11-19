def rombo_solido(n):
    if n < 2:
        print("La altura debe ser mayor o igual a 2.")
        return
    for i in range(n):
        espacios_izq = n - i - 1
        asteriscos = 2 * i + 1
        print(" " * espacios_izq + "*" * asteriscos)

    for i in range(n - 2, -1, -1):
        espacios_izq = n - i - 1
        asteriscos = 2 * i + 1
        print(" " * espacios_izq + "*" * asteriscos)

rombo_solido(4)
