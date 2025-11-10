"""
Dibuja un ordinograma de un programa que lea 100 números no nulos y luego muestre un
mensaje de si ha leído número negativo o no.
"""
ha_leido_negativo = False
contador = 0

while contador < 100:
    numero = float(input(f"Introduce el número {contador + 1}: "))
    
    if numero == 0:
        print("El número no puede ser cero. Intenta de nuevo.")
        continue

    if numero < 0:
        ha_leido_negativo = True

    contador += 1

if ha_leido_negativo:
    print("Se ha leído al menos un número negativo.")
else:
    print("No se ha leído ningún número negativo.")
