nota_10 = False
while True:
    nota = int(input("Introduce una nota (0-10, -1 para terminar): "))
    if nota == -1:
        break
    if nota == 10:
        nota_10 = True
if nota_10:
    print("Se ha introducido al menos una nota con valor 10")
else:
    print("No se ha introducido ninguna nota con valor 10")