h = int(input("Introduce horas: "))
m = int(input("Introduce minutos: "))
s = int(input("Introduce segundos: "))
s += 1
if s == 60:
    s = 0
    m += 1
if m == 60:
    m = 0
    h += 1
if h == 24:
    h = 0
print("Hora resultante:", h, ":", m, ":", s)