"""
Dibuja un ordinograma de un programa que lea 100 números no nulos y luego muestre un
mensaje indicando cuántos son positivos y cuantos negativos.
"""
positivos = 0
negativos = 0
contador = 0

while contador < 100:
    numero = int(input(f"Introduce el número {contador + 1}: "))

    if numero == 0:
        print("El número no puede ser cero. Intenta de nuevo.")
        continue 

    if numero > 0:
        positivos += 1
    else:
        negativos += 1

    contador += 1

print(f"Números positivos: {positivos}")
print(f"Números negativos: {negativos}")
