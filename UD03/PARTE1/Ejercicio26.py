import random
d1 = random.randint(1, 6)
d2 = random.randint(1, 6)
d3 = random.randint(1, 6)
print("Dados:", d1, d2, d3)
seis = [d1, d2, d3].count(6)
if seis == 3:
    print("Excelente")
elif seis == 2:
    print("Muy bien")
elif seis == 1:
    print("Regular")
else:
    print("Pésimo")