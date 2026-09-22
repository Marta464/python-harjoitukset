from math import pi
def pizza(num, hinta):
    m = num / 100
    h = m / 2
    p = pi*(h*h)
    c = hinta / p
    f = round(c, 2)
    return f
num = float(input("Syötä halkaisija: "))
hinta = float(input("Syötä hinta: "))
pizza1 = float(num, hinta)
num = float(input("Syötä seuraava halkaisija: "))
hinta = float(input("Syötä seuraava hinta: "))
pizza2 = float(num, hinta)
if pizza1 > pizza2:
    print(f"Pizza 2 {pizza2}€/neliömetri on halvempi kun pizza 1 {pizza1}€/neliömetri")
else:print(f"Pizza 1 {pizza1}€/neliömetri on halvempi kun pizza 2 {pizza2}€/neliömetri")