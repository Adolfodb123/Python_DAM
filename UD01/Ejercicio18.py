"""
Dibuja un ordinograma de un programa que lea dos números y nos diga cual es mayor o si
son iguales.
"""

num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

if num1 > num2:
    print(f"El mayor es: {num1}")
elif num2 > num1:
    print(f"El mayor es: {num2}")
else:
    print("Ambos números son iguales")