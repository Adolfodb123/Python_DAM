compra = float(input("Introduce el monto de compra: "))
dia = input("Introduce el día de la semana: ").lower()
if dia == "martes" or dia == "jueves":
    total = compra * 0.85
    print("Descuento aplicado. Total a pagar:", total)
else:
    print("Total a pagar:", compra)