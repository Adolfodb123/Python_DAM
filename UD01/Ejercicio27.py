"""
Dibuja un ordinograma de un programa que lea una secuencia de notas (con valores que
van de 0 a 10) que termina con el valor -1 y nos dice si hubo o no alguna nota con valor 10.
"""

hay_nota_10 = False

while True:
    nota = float(input("Introduce una nota (0 a 10, -1 para terminar): "))

    if nota == -1:
        break

    if nota < 0 or nota > 10:
        print("Nota inválida. Debe estar entre 0 y 10.")
        continue

    if nota == 10:
        hay_nota_10 = True

if hay_nota_10:
    print("Se ha introducido al menos una nota con valor 10.")
else:
    print("No se ha introducido ninguna nota con valor 10.")
