"""
Dibuja un ordinograma de un programa que dada una cantidad de euros que el usuario
introduce por teclado (múltiplo de 5 €) mostrará los billetes de cada tipo que serán necesarios
para alcanzar dicha cantidad (utilizando billetes de 500, 200, 100, 50, 20, 10 y 5). Hay que indicar
el mínimo de billetes posible. Por ejemplo, si el usuario introduce 145 el programa indicará que
UD 1 Introducción a la Programación Página 9 de 10
Juan Sevillano Hernández
será necesario 1 billete de 100 €, 2 billetes de 20 € y 1 billete de 5 € (no será válido por ejemplo
29 billetes de 5, que aunque sume 145 € no es el mínimo número de billetes posible).
"""
cantidad = int(input("Introduce una cantidad en euros (múltiplo de 5): "))

if cantidad % 5 != 0:
    print("La cantidad debe ser múltiplo de 5.")
else:
    billetes = [500, 200, 100, 50, 20, 10, 5]
    resultado = {}

    for billete in billetes:
        cantidad_billetes = cantidad // billete
        if cantidad_billetes > 0:
            resultado[billete] = cantidad_billetes
            cantidad %= billete

    print("\nDesglose mínimo de billetes:")
    for billete, cantidad_billetes in resultado.items():
        print(f"{cantidad_billetes} billete(s) de {billete} €")
