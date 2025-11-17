N = int(input("Introduce un número positivo: "))
factorial = 1
for i in range(1, N+1):
    factorial *= i
print("Factorial de", N, "es:", factorial)