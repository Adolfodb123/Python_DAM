def piramide_huecos(n):
    if n < 2:
        print("La altura debe ser mayor o igual a 2.")
        return

    for i in range(n - 1):
        espacios_izq = n - i - 1 
        if i == 0:
            print(" " * espacios_izq + "*")
        elif i == 1:
            print(" " * espacios_izq + "* *")
        elif i == 3:
            print(" " * espacios_izq + "* * * *")
        else:
            huecos = 2 * i - 1
            print(" " * espacios_izq + "*" + " " * huecos + "*")
            
    print("*" * (2 * n - 1))

piramide_huecos(6)
