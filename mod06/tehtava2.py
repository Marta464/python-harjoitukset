syote = input("Anna luku (tyhjä lopettaa): ")


luvut = []


while syote != "":
    luku = float(syote)  
    luvut.append(luku)   
    syote = input("Anna luku (tyhjä lopettaa): ")

luvut.sort(reverse=True)

for alkio in luvut[:5]:
    print(alkio)