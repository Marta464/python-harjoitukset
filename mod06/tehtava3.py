luku = int(input("Anna kokonaisluku: "))

on_alkuluku = True

if luku < 2:
    on_alkuluku = False
else:
     for i in range(2, luku):
        if luku % i == 0:
            on_alkuluku = False
            break
        
if on_alkuluku == True:
    print(f"Luku {luku} on alkuluku.")
else:
    print(f"Luku {luku} ei ole alkuluku.")