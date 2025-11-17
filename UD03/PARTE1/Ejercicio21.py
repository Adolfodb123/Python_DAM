nombre = input("Introduce el nombre del trabajador: ")
horas = float(input("Introduce las horas trabajadas: "))
tarifa = float(input("Introduce la tarifa por hora: "))
if horas <= 35:
    bruto = horas * tarifa
else:
    bruto = 35 * tarifa + (horas - 35) * tarifa * 1.5
if bruto <= 500:
    neto = bruto
elif bruto <= 900:
    neto = 500 + (bruto - 500) * 0.75
else:
    neto = 500 + 400 * 0.75 + (bruto - 900) * 0.55
print("Trabajador:", nombre)
print("Salario bruto:", bruto)
print("Salario neto:", neto)