"""
Dibuja un ordinograma de un programa que lea una secuencia de números no nulos hasta
que se introduzca un 0, y luego muestre si ha leído algún número negativo, cuantos positivos y
cuantos negativos.
"""
positivos = 0
negativos = 0
ha_leido_negativo = False

while True:
    numero = int(input("Introduce un número (0 para terminar): "))

    if numero == 0:
        break

    if numero > 0:
        positivos += 1
    else:
        negativos += 1
        ha_leido_negativo = True

print(f"Números positivos leídos: {positivos}")
print(f"Números negativos leídos: {negativos}")

if ha_leido_negativo:
    print("Se ha leído al menos un número negativo.")
else:
    print("No se ha leído ningún número negativo.")
