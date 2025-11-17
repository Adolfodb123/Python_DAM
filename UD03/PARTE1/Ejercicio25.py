nombre = input("Introduce el nombre del postulante: ")
facultad = input("Introduce la facultad: ").lower()
if facultad == "ingenieria":
    importe = 500
    mensualidad = 800
elif facultad == "medicina":
    importe = 700
    mensualidad = 1000
elif facultad == "derecho":
    importe = 400
    mensualidad = 600
else:
    importe = 300
    mensualidad = 500
igv = (importe + mensualidad) * 0.18
total = importe + mensualidad + igv
print("Postulante:", nombre)
print("Importe:", importe)
print("Mensualidad:", mensualidad)
print("IGV:", igv)
print("Monto final:", total)