cantidad = int(input("Introduce una cantidad en euros (múltiplo de 5): "))
billetes = [500, 200, 100, 50, 20, 10, 5]
resultado = {}
for b in billetes:
    if cantidad >= b:
        num_billetes = cantidad // b
        cantidad = cantidad % b
        resultado[b] = num_billetes
for b, n in resultado.items():
    print(f"{n} billete(s) de {b} €")