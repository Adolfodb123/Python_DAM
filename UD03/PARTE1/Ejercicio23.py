compra = float(input("Introduce el valor de compra: "))
pago = input("Forma de pago (contado/tarjeta): ")
if pago == "contado":
    total = compra * 0.95
    print("Descuento aplicado. Total a pagar:", total)
elif pago == "tarjeta":
    total = compra * 1.03
    print("Recargo aplicado. Total a pagar:", total)