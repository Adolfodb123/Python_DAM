"""
Dibuja un ordinograma que calcula el salario neto semanal de un trabajador en función del
número de horas trabajadas y la tasa de impuestos de acuerdo a las siguientes hipótesis:
• Las primeras 35 horas se pagan a tarifa normal.
• Las horas que pasen de las 35 horas se pagan a 1,5 veces la tarifa normal.
• Las tasas de impuesto son:
o Los primeros 500€ son libres de impuestos.
o Los siguientes 400€ tiene un 25% de impuesto.
o Los restantes un 45% de impuesto.
Escribe el nombre del trabajador, salario bruto, tasas y salario neto.
"""

nombre = input("Introduce el nombre del trabajador: ")
horas_trabajadas = float(input("Introduce el número de horas trabajadas: "))
tarifa = float(input("Introduce la tarifa por hora (€): "))

if horas_trabajadas <= 35:
    salario_bruto = horas_trabajadas * tarifa
else:
    horas_normales = 35
    horas_extra = horas_trabajadas - 35
    salario_bruto = (horas_normales * tarifa) + (horas_extra * tarifa * 1.5)

impuestos = 0
restante = salario_bruto

if restante > 500:
    restante -= 500
else:
    restante = 0

if restante > 0:
    tramo = min(restante, 400)
    impuestos += tramo * 0.25
    restante -= tramo

if restante > 0:
    impuestos += restante * 0.45

salario_neto = salario_bruto - impuestos

print("\n--- RESUMEN SEMANAL ---")
print(f"Nombre del trabajador: {nombre}")
print(f"Salario bruto: {salario_bruto:.2f} €")
print(f"Impuestos: {impuestos:.2f} €")
print(f"Salario neto: {salario_neto:.2f} €")
