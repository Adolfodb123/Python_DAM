"""
Dibuja un ordinograma que dado el precio de un artículo y el precio de venta real nos
muestre el porcentaje de descuento realizado.

"""

precio_original = float(input("Introduce el precio original del artículo: "))
precio_venta = float(input("Introduce el precio de venta real: "))

descuento = precio_original - precio_venta
porcentaje_descuento = (descuento / precio_original) * 100

print("El porcentaje de descuento realizado es:", porcentaje_descuento, "%")
