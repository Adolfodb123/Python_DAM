"""
Dibuja un ordinograma de un programa que calcule y escriba la suma y el producto de los
10 primeros números naturales.
"""
suma = 0
producto = 1

for numero in range(1, 11):
    suma += numero
    producto *= numero

print(f"La suma de los 10 primeros números naturales es: {suma}")
print(f"El producto (factorial de 10) es: {producto}")
