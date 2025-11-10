"""
Dibuja un ordinograma que lea una calificación numérica entre 0 y 10 y la transforme en la
calificación alfabética, escribiendo el siguiente resultado.
• De 0 a < 3 Muy Deficiente.
• De 3 a < 5 Insuficiente.
• De 5 a < 6 Suficiente.
• De 6 a < 7 Bien.
• De 7 a <9 Notable.
• De 9 a 10 Sobresaliente.
"""
nota = float(input("Introduce una calificación entre 0 y 10: "))

if nota < 0 or nota > 10:
    print("La calificación debe estar entre 0 y 10.")
else:
    if nota < 3:
        print("Muy Deficiente")
    elif nota < 5:
        print("Insuficiente")
    elif nota < 6:
        print("Suficiente")
    elif nota < 7:
        print("Bien")
    elif nota < 9:
        print("Notable")
    else:
        print("Sobresaliente")
