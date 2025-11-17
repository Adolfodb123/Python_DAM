print("Piensa un número entre 1 y 100 y yo lo adivinaré.")
bajo = 1
alto = 100
while True:
    intento = (bajo + alto) // 2
    print("¿Es", intento, "?")
    respuesta = input("Responde mayor, menor o igual: ").lower()
    if respuesta == "igual":
        print("¡He adivinado tu número!")
        break
    elif respuesta == "mayor":
        bajo = intento + 1
    elif respuesta == "menor":
        alto = intento - 1
    else:
        print("Respuesta inválida, escribe mayor, menor o igual.")