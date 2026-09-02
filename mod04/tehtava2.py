matkustamoluokka = input("Anna matkustamoluokka: ")

if matkustamoluokka == "LUX":
    print("LUX on parvekkeellinen hytti yläkannella.")
elif matkustamoluokka == "A":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif matkustamoluokka == "B":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif matkustamoluokka == "C":
    print("C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka.")