A = int(input("Introduce el valor de A: "))
B = int(input("Introduce el valor de B: "))
resultado = 1
for i in range(B):
    resultado *= A
print(f"{A} elevado a {B} es:", resultado)