def nimi_funktio(parametr1, parametr2):
    tulos = parametr1 + parametr2
    return tulos

data1 = int(input("Anna luku 1: "))
data2  = int(int(input("Anna luku 2:")))
vastaus = nimi_funktio(data1, data2)

print(f"Tulos on {vastaus}.")