# PROJEKTI 1: Käyttäjätiedot
nimi = input("Anna nimesi: ")
ikä = int(input("Anna ikä: "))

print(f"Nimesi: {nimi}")
print(f"Ikä: {ikä}")

# PROJEKTI 2: Ikätarkistus ja päävalikko

if ikä >= 12:
    print("Tervetuloa pelaamaan, " + nimi + "!")

    peli_käynnissä = True
    while peli_käynnissä:
        print("\n--- PÄÄVALIKKO ---")
        print("Komennot: pelaa, pisteet, lopeta")
        
        komento = input("Syötä komento: ")
        
        if komento == "lopeta":
            print("Kiitos pelaamisesta! Ohjelma sammuu.")

            peli_käynnissä = False 
        elif komento == "pelaa":
            print("Peli alkaa... Valmistaudu!")
            
        elif komento == "pisteet":
            print("Ennätyspisteesi ovat: 100 pistettä.")
            
        else:
            print("Tuntematon komento. Yritä uudelleen.")

else:
    print("Olet alaikäinen. Ohjelma sammuu.")