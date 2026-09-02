import random

N = int(input("Anna pisteiden määrä: "))

n = 0
kerrat = 0

while kerrat < N:
     x = random.uniform(-1.0, 1.0)
     y = random.uniform(-1.0, 1.0)

     if x**2 + y**2 < 1:
        n = n + 1

     kerrat = kerrat + 1

pii = (4 * n) / N

print(f"Piin likiarvo on: {pii}")