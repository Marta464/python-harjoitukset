def luva(summa):
    tulos = 0
    for luku in summa:
        tulos = tulos + luku
    return tulos

alkuperainen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
summa_tulos = luva(alkuperainen)
print("Summa:", summa_tulos)