def luvu(lista):
    tulos = []
    for luku in lista:
        if luku % 2 == 0:
            tulos.append(luku)
    return tulos

alkuperainen= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
karsittu = luvu(alkuperainen)

print("Alkuperainen", alkuperainen)
print("Karsittu", karsittu)