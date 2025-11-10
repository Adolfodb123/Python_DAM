"""
Dibuja un ordinograma que lea dos números, calcule y muestre el valor de sus suma, resta,
producto y división (Ten en cuenta la división por cero).
"""

num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

suma = num1 + num2
print(f"Suma: {suma}")

resta = num1 - num2
print(f"Resta: {resta}")

producto = num1 * num2
print(f"Producto: {producto}")

if num2 != 0:
    division = num1 / num2
    print(f"División: {division}")
else:
    print("No se puede dividir entre cero.")
