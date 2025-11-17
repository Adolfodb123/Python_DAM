precio = float(input("Introduce el precio original: "))
venta = float(input("Introduce el precio de venta: "))
descuento = ((precio - venta) / precio) * 100
print("Descuento realizado:", descuento, "%")