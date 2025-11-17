nota = float(input("Introduce una calificación entre 0 y 10: "))
if 0 <= nota < 3:
    print("Muy Deficiente")
elif 3 <= nota < 5:
    print("Insuficiente")
elif 5 <= nota < 6:
    print("Suficiente")
elif 6 <= nota < 7:
    print("Bien")
elif 7 <= nota < 9:
    print("Notable")
elif 9 <= nota <= 10:
    print("Sobresaliente")
else:
    print("Nota inválida")