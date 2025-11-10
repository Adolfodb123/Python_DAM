"""
Dibuja un ordinograma que lea dos números, calcule y muestre el valor de sus suma, resta,
producto y división.

"""

num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

suma = num1 + num2
resta = num1 - num2
producto = num1 * num2

if num2 != 0:
    division = num1 / num2
else:
    division = "No se puede dividir entre cero"

print("Suma:", suma)
print("Resta:", resta)
print("Producto:", producto)
print("División:", division)
