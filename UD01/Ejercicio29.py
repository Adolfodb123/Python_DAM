"""
Dibuja un ordinograma de un programa donde el usuario “piensa” un número del 1 al 100
y el ordenador intenta adivinarlo. Es decir, el ordenador irá proponiendo números una y otra
vez hasta adivinarlo (El usuario deberá indicarlo al ordenador si es mayor o menor o igual al
número pensado).
"""

print("Piensa un número entre 1 y 100. El ordenador intentará adivinarlo.")
input("Presiona ENTER cuando estés listo...")

inferior = 1
superior = 100
intentos = 0

while True:
    intento = (inferior + superior) // 2
    intentos += 1
    print(f"¿Es {intento} tu número?")
    respuesta = input("Responde con 'mayor', 'menor' o 'igual': ").lower()

    if respuesta == "igual":
        print(f"¡El ordenador ha adivinado tu número {intento} en {intentos} intentos!")
        break
    elif respuesta == "mayor":
        inferior = intento + 1
    elif respuesta == "menor":
        superior = intento - 1
    else:
        print("Respuesta no válida. Usa 'mayor', 'menor' o 'igual'.")
