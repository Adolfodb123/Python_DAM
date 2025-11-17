import math
radio = float(input("Introduce el radio: "))
diametro = 2 * radio
circunferencia = math.pi * diametro
area = math.pi * radio**2
volumen = (4/3) * math.pi * radio**3
print("Circunferencia:", circunferencia)
print("Área del círculo:", area)
print("Volumen de la esfera:", volumen)