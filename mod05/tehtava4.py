import random

oikea_vastaus = random.randint(1, 10)

arvaus = 0

print("Olen jakanut luvun väliltä 1..10. Arvaa se!")

while arvaus != oikea_vastaus:
    arvaus = int(input("Anna arvaus: "))
    
    if arvaus > oikea_vastaus:
        print("Liian suuri arvaus")
    elif arvaus < oikea_vastaus:
        print("Liian pieni arvaus")
    else:
        print("Oikein")