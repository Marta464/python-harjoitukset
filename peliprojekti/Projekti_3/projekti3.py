# --- FUNKTIOT-3

def pelaa(tavarat):
    """Peli alkaa -toiminto, joka kysyy esineen reppuun."""
    print("Peli alkaa... Valmistaudu!")
    uusi_esine = input("Löysit esineen! Minkä esineen haluat lisätä reppuun? ")
    if uusi_esine.strip() != "":
        tavarat.append(uusi_esine)
        print(f"'{uusi_esine}' on lisätty reppuun!\n")
    else:
        print("Esineen nimi ei voi olla tyhjä.\n")

def nayta_pisteet():
    """Tulostaa ennätyspisteet."""
    print("Ennätyspisteesi ovat: 100 pistettä.\n")

def nayta_inventaario(tavarat):
    """Tulostaa reppuun kerätyt tavarat."""
    print("--- REPUN SISÄLTÖ ---")
    if not tavarat:
        print("Reppusi on tyhjä.")
    else:
        for esine in tavarat:
            print(f"- {esine}")
    print("---------------------\n")


# --- PÄÄOHJELMA-1/2

nimi = input("Anna nimesi: ")
ika = int(input("Anna ikä: "))

print(f"Nimesi: {nimi}")
print(f"Ikä: {ika}")

reppu = []

if ika >= 12:
    print("Tervetuloa pelaamaan, " + nimi + "!")
    
    peli_käynnissä = True
    while peli_käynnissä:
        print("\n--- PÄÄVALIKKO ---")
        print("Komennot: pelaa, pisteet, reppu, lopeta")
        
        komento = input("Syötä komento: ")
        
        if komento == "lopeta":
            print("Kiitos pelaamisesta! Ohjelma sammuu.")
            peli_käynnissä = False
        elif komento == "pelaa":
            pelaa(reppu)
        elif komento == "pisteet":
            nayta_pisteet()
        elif komento == "reppu":
            nayta_inventaario(reppu)
        else:
            print("Tuntematon komento. Yritä uudelleen.")
else:
    print("Olet alaikäinen. Ohjelma sammuu.")
    