syote = input("Anna kaupunki (tyhjä lopettaa): ")

kaupungit = []

for i in range(5):
    nimi = input("Anna kaupungin nimi: ")
    kaupungit.append(nimi)


print("\nSyötetyt kaupungit:")
for kaupunki in kaupungit:
    print(kaupunki)