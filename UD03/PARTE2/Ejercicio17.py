suma_pares = 0
suma_impares = 0
for i in range(100, 201):
    if i % 2 == 0:
        suma_pares += i
    else:
        suma_impares += i
print("Suma de pares:", suma_pares)
print("Suma de impares:", suma_impares)