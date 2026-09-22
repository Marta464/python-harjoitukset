lentoasemat = {}

while True:
    print("\nValitse toiminto:")
    print("1 - Syötä uusi lentoasema")
    print("2 - Hae lentoaseman tiedot")
    print("3 - Lopeta")
    
    valinta = input("Valinta (1, 2 tai 3): ")
    
    if valinta == "1":
        koodi = input("Syötä lentoaseman ICAO-koodi: ")
        nimi = input("Syötä lentoaseman nimi: ")
        lentoasemat[koodi] = nimi
        print("Lentoasema tallennettu!")
        
    elif valinta == "2":
        haku_koodi = input("Syötä haettavan lentoaseman ICAO-koodi: ")
        if haku_koodi in lentoasemat:
            print(f"Lentoaseman nimi: {lentoasemat[haku_koodi]}")
        else:
            print("Lentoasemaa ei löydy!")
    
    elif valinta == "3":
        print("Ohjelma sammuu. Kiitos!")
        break 

    else:
        print("Virheellinen valinta, yritä uudelleen.")
