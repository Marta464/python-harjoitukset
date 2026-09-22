from esine import Esine
from huone import Huone
from pelaaja import Pelaaja
import os

def nayta_pisteet():
    print("Ennätyspisteesi ovat: 100 pistettä.\n")

def main():
    nimi = input("Anna nimesi: ")
    ika = int(input("Anna ikä: "))


    print(f"Nimesi: {nimi}")
    print(f"Ikä: {ika}")

    if ika < 12:
        print("Ola alaikäinen. Ohjelma sammu.")
        return


    with open("peliprojekti/projekti_4/intro.txt", "r", encoding="utf-8") as f:
        teksti = f.read()
        print(teksti)

    with open("peliprojekti/projekti_4/ohjet.txt", "r", encoding="utf-8") as f:
        ohje_teksti = f.read()
        print(ohje_teksti)
        
        avain = Esine("Kulta-avain", 0.2)
        miekka = Esine("Miekka", 3.5)

        aula = Huone("Pääula", esine=avain)
        luola = Huone("Pimeä luola", esine=miekka)

        if os.path.exists("peliprojekti/projekti_4/tallenna.txt"):
            jatketaan = input("Löydettii tallennettu peli. Haluatko jatka? (kyllä/ei) : ").strip().lower()
            if jatketaan == "kyllä":
                with open("peliprojekti/projekti_4/tallenna.txt", "r", encoding="utf-8") as f:
                    tiedot = f.read().split(",")
                    nimi = tiedot[0]

                    if len(tiedot) > 1 and tiedot[1] == "Pimeä luola":
                        aloitus_sijainti = luola
                    else:
                        aloitus_sijainti = aula

                    print(f"Tervetuloa takaisin; {nimi}!")
            else:
                aloitus_sijainti = aula
        else:
            aloitus_sijainti = aula

        print("Tervetuloa pelaamaan, " + nimi + "!")
        pelaaja = Pelaaja(nimi, aloitus_sijanti=aloitus_sijainti)

        peli_kaynnissa = True

        while peli_kaynnissa:
            print(f"\n--- Påäävalikko (sijainti: {pelaaja.sijanti.nimi}) ---")
            print("Komennot: pelaa, liiku, pisteet, reppu, lopeta")

            komento = input ("Syötä komento: ").strip().lower()

            if komento == "lopeta":
                with open("tallenna.txt", "w", encoding="utf-8") as f:
                    tavarat = ",".join([e.nimi for e in pelaaja.esineet])
                    f.write(f"{pelaaja.nimi},{pelaaja.sijanti.nimi},{tavarat}")

                print("Peli tallennettu!")
                print("Kiitos pelaamisesta! Ohjelma sammu.")
                peli_kaynnissa = False

            elif komento == "pelaa":
                print("Peli alkaa... Valmistaudu!")
                pelaaja.keraa_esine()

            elif komento == "liiku":
                if pelaaja.sijanti == aula:
                    pelaaja.liiku(luola)
                else:
                    pelaaja.liiku(aula)

            elif komento == "pisteet":
                nayta_pisteet()

            elif komento == "reppu":
                pelaaja.nayta_inventaario()

            else:
                print("Tuntematon komento. Yritä uudelleen.")

if __name__== "__main__":
    main()