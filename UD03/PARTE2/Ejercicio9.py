positivos = 0
negativos = 0
hay_negativo = False
while True:
    num = int(input("Introduce un número (0 para terminar): "))
    if num == 0:
        break
    if num > 0:
        positivos += 1
    else:
        negativos += 1
        hay_negativo = True
print("Positivos:", positivos)
print("Negativos:", negativos)
if hay_negativo:
    print("Se ha leído algún número negativo")
else:
    print("No se ha leído ningún número negativo")