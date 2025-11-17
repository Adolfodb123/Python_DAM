negativo = False
for i in range(100):
    num = int(input(f"Introduce el número {i+1}: "))
    if num < 0:
        negativo = True
if negativo:
    print("Se ha leído algún número negativo")
else:
    print("No se ha leído ningún número negativo")